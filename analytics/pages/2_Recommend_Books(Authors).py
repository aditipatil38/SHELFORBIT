import streamlit as st
import sqlite3

# Connect to the DB
conn = sqlite3.connect("25k.db")
cursor = conn.cursor()

# --- Functions ---
def get_genres():
    cursor.execute("SELECT genre_id, genre FROM genres")
    return cursor.fetchall()

def get_authors_by_genres(genre_ids):
    if not genre_ids:
        return []
    placeholders = ','.join(['?'] * len(genre_ids))
    query = f"""
        SELECT DISTINCT a.author_id, a.author
        FROM authors a
        JOIN book_authors ba ON a.author_id = ba.author_id
        JOIN book_genres bg ON ba.book_id = bg.book_id
        WHERE bg.genre_id IN ({placeholders})
    """
    cursor.execute(query, genre_ids)
    return cursor.fetchall()

def get_books(author_ids, genre_ids, min_rating):
    if not author_ids or not genre_ids:
        return []

    author_placeholders = ','.join(['?'] * len(author_ids))
    genre_placeholders = ','.join(['?'] * len(genre_ids))

    query = f"""
        SELECT 
            b.book_id,
            b.title,
            group_concat(DISTINCT a.author) AS authors,
            group_concat(DISTINCT g.genre) AS genres,
            p.publisher,
            br.rating
        FROM books b
        JOIN book_authors ba ON b.book_id = ba.book_id
        JOIN authors a ON ba.author_id = a.author_id
        JOIN book_genres bg ON b.book_id = bg.book_id
        JOIN genres g ON bg.genre_id = g.genre_id
        JOIN book_ratings br ON b.book_id = br.book_id
        LEFT JOIN book_publishers bp ON b.book_id = bp.book_id
        LEFT JOIN publishers p ON bp.publisher_id = p.publisher_id
        WHERE ba.author_id IN ({author_placeholders})
        AND bg.genre_id IN ({genre_placeholders})
        AND br.rating >= ?
        GROUP BY b.book_id
    """
    params = author_ids + genre_ids + [min_rating]
    cursor.execute(query, params)
    return cursor.fetchall()



# --- UI ---
st.title(" Book Recommender")
def display_books_as_cards(books, cards_per_row=3):
    for i in range(0, len(books), cards_per_row):
        cols = st.columns(cards_per_row)
        for col, book in zip(cols, books[i:i+cards_per_row]):
            book_id, title, authors, genres, publisher, rating = book
            with col:
                st.markdown(f"""
                        <div style="
                        border: 1px solid rgba(255, 255, 255, 0.2); 
                        border-radius: 15px; 
                        padding: 25px; 
                        background-color: rgba(255, 255, 255, 0.05); 
                        margin: 10px 5px; 
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                        backdrop-filter: blur(5px);
                        word-wrap: break-word;
                    ">
                        <h4 style="margin-bottom: 8px;">📘 {title}</h4>
                        <p style="margin: 4px 0;"><b> Author:</b> {authors}</p>
                        <p style="margin: 4px 0;"><b> Genre:</b> {genres}</p>
                        <p style="margin: 4px 0;"><b> Publisher:</b> {publisher if publisher else "Unknown"}</p>
                        <p style="margin: 4px 0;"><b>⭐ Rating:</b> {rating:.2f}</p>
                    </div>
                """, unsafe_allow_html=True)


genres = get_genres()
genre_map = {name: gid for gid, name in genres}
selected_genres = st.multiselect("Select Genre(s)", list(genre_map.keys()))

if selected_genres:
    genre_ids = [genre_map[name] for name in selected_genres]
    authors = get_authors_by_genres(genre_ids)
    author_map = {name: aid for aid, name in authors}
    selected_authors = st.multiselect("Select Author(s)", list(author_map.keys()))

    if selected_authors:
        author_ids = [author_map[name] for name in selected_authors]
        min_rating = st.slider(
            "Minimum Rating",
            min_value=1.0,
            max_value=5.0,
            value=3.0,
            step=0.01,
            format="%.2f"
        )

        books = get_books(genre_ids, author_ids, min_rating)
        st.subheader(" Recommended Books")
        if books:
            display_books_as_cards(books)
        else:
            st.info("No books match the selected filters.")

