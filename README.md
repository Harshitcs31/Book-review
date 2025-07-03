#  Book Review API

A simple REST API built with FastAPI + SQLAlchemy + Alembic + SQLite.

---

##  Features

- `GET /books`: List all books
- `POST /books`: Add a new book
- `GET /books/{id}/reviews`: List reviews for a book
- `POST /books/{id}/reviews`: Add a review to a book

---

##  Tech Stack

- FastAPI
- SQLite (with SQLAlchemy ORM)
- Alembic for DB migrations
- Pytest for testing

---

##  Setup Instructions
#Create Virtual Environment
python -m venv venv

# Install Dependencies
pip install -r requirements.txt

# Database Setup
## Initialize Alembic

alembic init alembic
## Set alembic.ini
sqlalchemy.url = sqlite:///./books.db

# Generate Migrations
alembic revision --autogenerate -m "Initial schema"


# Running Tests
Run the unit and integration tests:


pytest tests/test_main.py -v


##Run the API

uvicorn app.main:app --reload

