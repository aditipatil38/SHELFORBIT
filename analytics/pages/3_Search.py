import streamlit as st
import sqlite3

conn = sqlite3.connect("25k.db", check_same_thread=False)
cursor = conn.cursor()

def search_books_by_title(keyword):
    cursor.execute("""
        SELECT b.book_id, b.title
        FROM books b
        WHERE LOWER(b.title) LIKE ?
    """, (f"%{keyword.lower()}%",))
    return cursor.fetchall()

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

def paginate(data, page_size, page_number):
    start = (page_number - 1) * page_size
    end = start + page_size
    return data[start:end], len(data)

st.title("🔍 Book Search")

keyword = st.text_input("Enter book title to search")

if keyword:
    results = search_books_by_title(keyword)

    if results:
        st.subheader("📘 Matching Titles")

        page_size = 5
        total = len(results)
        page_num = st.number_input("Page", min_value=1, max_value=(total - 1) // page_size + 1, step=1)

        paged_results, _ = paginate(results, page_size, page_num)

        for book_id, title in paged_results:
            genres, tags = get_genres_and_tags(book_id)

            st.markdown(f"### {title}")
            st.markdown(f"**Genres:** {', '.join(genres) if genres else 'None'}")
            st.markdown(f"**Tags:** {', '.join(tags) if tags else 'None'}")

            if st.button("🔁 See Similar Books", key=f"similar_{book_id}"):
                st.session_state.selected_book_id = book_id
                st.switch_page("pages/4_Similar.py")

            st.markdown("---")
    else:
        st.warning("No books found.")
