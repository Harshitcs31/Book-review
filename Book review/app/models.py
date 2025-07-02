from sqlalchemy import Column, Integer, String, Text, ForeignKey, Index
from sqlalchemy.orm import relationship
from .database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    reviews = relationship("Review", back_populates="book")

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"))  # Do NOT use index=True here
    reviewer = Column(String, nullable=False)
    comment = Column(Text, nullable=False)

    book = relationship("Book", back_populates="reviews")

# ✅ Define index ONCE here
Index("ix_reviews_book_id", Review.book_id)
