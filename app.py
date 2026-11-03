from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
books = [
    {
        "id": 1,
        "title": "Python Programming",
        "author": "John Smith",
        "availability": "Available"
    },
    {
        "id": 2,
        "title": "Advanced Python",
        "author": "David Brown",
        "availability": "Available"
    },
    {
        "id": 3,
        "title": "Machine Learning Basics",
        "author": "Andrew Miller",
        "availability": "Available"
    },
    {
        "id": 4,
        "title": "Introduction to Physics",
        "author": "Robert Wilson",
        "availability": "Available"
    },
    {
        "id": 5,
        "title": "Data Science with Python",
        "author": "Sarah Johnson",
        "availability": "Available"
    }
]

def get_recommendations(book_id):
        selected_book = None

        for book in books:
            if book["id"] == book_id:
                selected_book = book
                break
        if selected_book is None:
            return []
        book_texts = []

        for book in books:
            text = book["title"] + " " + book["author"]
            book_texts.append(text)                        

        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(book_texts) 

        similarity_scores = cosine_similarity(tfidf_matrix)
        selected_index = books.index(selected_book)
        similarity_scores = similarity_scores[selected_index] 
        similar_book_indexes = similarity_scores.argsort()[::-1]

        recommendations = []

        for index in similar_book_indexes:
            if index != selected_index:
                recommendations.append({
                    "book": books[index],
                    "score": round(similarity_scores[index], 2)
                })

            if len(recommendations) == 5:
                break

        return recommendations
@app.route('/')
def home():
    return render_template("login.html")

@app.route('/user_dashboard')
def user_dashboard():
    return render_template("user_dashboard.html", books=books)


@app.route('/login', methods = ['POST'])
def login():
    user_id = request.form['user_id']
    password = request.form['password']
    role = request.form['role']
    # Add your login logic here
    if role == 'admin' and user_id == 'admin' and password == 'admin123':
        return render_template("admin_dashboard.html", books=books)
    elif role == 'user' and user_id == 'user' and password == 'user123':
        return render_template("user_dashboard.html", books=books)
    else:
        return "Invalid User ID, Password, or Role" 
@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']

    new_id = len(books) + 1

    new_book = {
        "id": new_id,
        "title": title,
        "author": author,
        "availability": "Available"
    }

    books.append(new_book)

    return render_template("admin_dashboard.html", books=books)    

@app.route('/borrow_book/<int:book_id>', methods=['POST'])
def borrow_book(book_id):
    for book in books:
        if book["id"] == book_id:
            if book["availability"] == "Available":
                book["availability"] = "Borrowed"
                return render_template("user_dashboard.html", books=books)
            else:
                return "Book is already borrowed"

    return "Book not found"


@app.route('/return_book/<int:book_id>', methods=['POST'])
def return_book(book_id):
    for book in books:
        if book["id"] == book_id:
            if book["availability"] == "Borrowed":
                book["availability"] = "Available"
                return render_template("user_dashboard.html", books=books)
            else:
                return "Book is already available"

    return "Book not found"

@app.route('/check_availability', methods=['POST'])
def check_availability():
    book_title = request.form['book_title'].strip()

    for book in books:
        if book["title"].lower() == book_title.lower():
            return f"'{book['title']}' is {book['availability']}"

    return f"'{book_title}' is Not Found"

@app.route('/recommend', methods=['POST'])
def recommend():
    book_id = int(request.form['book_id'])

    recommendations = get_recommendations(book_id)

    selected_book = next(
        book for book in books if book["id"] == book_id
    )

    return render_template(
        "recommendations.html",
        selected_book=selected_book,
        recommendations=recommendations
    )
    
if __name__ == '__main__':
    app.run(debug=True)