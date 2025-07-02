from sqlalchemy.orm import Session
from . import models, schemas

def get_books(db: Session):
    return db.query(models.Book).all()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_reviews_by_book(db: Session, book_id: int):
    return db.query(models.Review).filter(models.Review.book_id == book_id).all()

def create_review(db: Session, book_id: int, review: schemas.ReviewCreate):
    db_review = models.Review(book_id=book_id, **review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review
