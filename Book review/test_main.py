# tests/test_main.py

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app.main import app
from app import models

# -------------------------------
# 1. Test Database Setup
# -------------------------------

SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///:memory:"


engine = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Create the schema
Base.metadata.create_all(bind=engine)

# -------------------------------
# 2. Dependency Override for Testing
# -------------------------------

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Inject test DB into the app
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

# -------------------------------
# 3. Unit Test: POST /books
# -------------------------------

def test_create_book():
    response = client.post("/books", json={
        "title": "Test Book",
        "author": "Test Author",
        "description": "A simple test book"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Book"
    assert data["author"] == "Test Author"
    assert "id" in data

# -------------------------------
# 4. Unit Test: GET /books
# -------------------------------

def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    books = response.json()
    assert isinstance(books, list)
    assert any(book["title"] == "Test Book" for book in books)

# -------------------------------
# 5. Integration Test: Simulated DB-only fetch
# -------------------------------

def test_integration_books_fetch_no_cache():
    # Clear the DB first
    db = next(override_get_db())
    db.query(models.Book).delete()
    db.commit()

    # Manually insert a book
    book = models.Book(title="Integration Book", author="Test Integration")
    db.add(book)
    db.commit()
    db.refresh(book)

    # Now call the endpoint (simulating no cache, only DB read)
    response = client.get("/books")
    assert response.status_code == 200
    data = response.json()
    assert any(b["title"] == "Integration Book" for b in data)
