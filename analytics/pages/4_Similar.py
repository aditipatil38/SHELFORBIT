import streamlit as st
import sqlite3

conn = sqlite3.connect("25k.db", check_same_thread=False)
cursor = conn.cursor()

book_id = st.session_state.get("selected_book_id")
if book_id is None:
    st.warning("No book selected. Please search and select a book first.")
    st.stop()

def get_genres_and_tags(book_id):
    cursor.execute("""
        SELECT g.genre
        FROM book_genres bg JOIN genres g ON bg.genre_id = g.genre_id
        WHERE bg.book_id = ?
    """, (book_id,))
    genres = [g[0] for g in cursor.fetchall()]

    cursor.execute("""
        SELECT t.tag
        FROM book_tags bt JOIN tags t ON bt.tag_id = t.tag_id
        WHERE bt.book_id = ?
    """, (book_id,))
    tags = [t[0] for t in cursor.fetchall()]

    return genres, tags

def get_books_by_genres_and_tags(genres, tags, exclude_book_id):
    where_clauses = []
    params = []

    if genres:
        placeholders = ','.join(['?'] * len(genres))
        where_clauses.append(f"g.genre IN ({placeholders})")
        params.extend(genres)

    if tags:
        placeholders = ','.join(['?'] * len(tags))
        where_clauses.append(f"t.tag IN ({placeholders})")
        params.extend(tags)

    if not where_clauses:
        return []

    query = f"""
        SELECT DISTINCT b.book_id, b.title
        FROM books b
        LEFT JOIN book_genres bg ON b.book_id = bg.book_id
        LEFT JOIN genres g ON bg.genre_id = g.genre_id
        LEFT JOIN book_tags bt ON b.book_id = bt.book_id
        LEFT JOIN tags t ON bt.tag_id = t.tag_id
        WHERE ({' OR '.join(where_clauses)}) AND b.book_id != ?
    """
    params.append(exclude_book_id)
    cursor.execute(query, params)
    return cursor.fetchall()

def paginate(data, page_size, page_number):
    start = (page_number - 1) * page_size
    end = start + page_size
    return data[start:end], len(data)

# --- UI ---
cursor.execute("SELECT title FROM books WHERE book_id = ?", (book_id,))
row = cursor.fetchone()

if row:
    title = row[0]
    genres, tags = get_genres_and_tags(book_id)

    st.title("🔁 Similar Books")
    st.markdown(f"### Based on: **{title}**")
    st.markdown(f"**Genres:** {', '.join(genres) if genres else 'None'}")
    st.markdown(f"**Tags:** {', '.join(tags) if tags else 'None'}")

    similar_books = get_books_by_genres_and_tags(genres, tags, book_id)

    if similar_books:
        page_size = 5
        page_num = st.number_input("Page", min_value=1, max_value=(len(similar_books) - 1) // page_size + 1, step=1)
        rec_paged, total = paginate(similar_books, page_size, page_num)

        for bid, btitle in rec_paged:
            st.markdown(f"- {btitle}")
        st.caption(f"Showing {len(rec_paged)} of {total} similar books.")
    else:
        st.info("No similar books found.")
else:
    st.error("Invalid book ID.")

if st.button("⬅️ Back to Search"):
    st.switch_page("pages/3_Search.py")
