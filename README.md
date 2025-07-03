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

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/book-review-api.git
cd book-review-api
