# AI Recommendation Library Management System

A web-based Library Management System built with Python and Flask,
featuring AI-based book recommendations using TF-IDF and cosine similarity.

## Features
- Role-based login (Admin and User)
- Admin dashboard: add new books to the library
- User dashboard: view books, borrow and return books
- Check a book's availability by title
- AI book recommendations: suggests similar books based on the
  title and author, using TF-IDF vectorization and cosine similarity

## Tech Stack
- Python
- Flask
- scikit-learn (TF-IDF, cosine similarity)
- HTML templates (Jinja2)

## How the Recommendation System Works
1. Each book's title and author are combined into one text string.
2. TF-IDF converts the text into numerical vectors.
3. Cosine similarity compares the selected book with all others.
4. The most similar books are shown as recommendations with a score.

## How to Run
1. Clone the repository:
   `git clone https://github.com/shymafathima/ai-recommendation-library-management-system.git`
2. Install dependencies:
   `pip install -r requirements.txt`
3. Run the app:
   `python app.py`
4. Open http://127.0.0.1:5000 in your browser.

## Demo Login Credentials
| Role  | User ID | Password |
|-------|---------|----------|
| Admin | admin   | admin123 |
| User  | user    | user123  |

(Demo credentials for testing only.)

## Notes
Book data is stored in memory, so changes reset when the app restarts.

## Future Improvements
- Connect a database (SQLite or MySQL) for permanent storage
- Secure login with password hashing
- Recommendations based on book descriptions and genres
