from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Book table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)  # Fix: 259 -> 250
    rating = db.Column(db.Float, nullable=False)

# **Fix**: Ensure database is created inside an application context
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # Create new book record
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=float(request.form["rating"])  # Convert rating to float
        )

        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))  # Redirect to home page after submission

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
