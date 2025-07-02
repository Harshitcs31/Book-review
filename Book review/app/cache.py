import redis
import json
from typing import List
from .schemas import Book

# Connect to Redis
try:
    redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
    redis_client.ping()  # test connection
    redis_available = True
except redis.exceptions.ConnectionError:
    redis_client = None
    redis_available = False

BOOK_CACHE_KEY = "books_cache"

def get_cached_books() -> List[Book] | None:
    if not redis_available:
        return None

    cached_data = redis_client.get(BOOK_CACHE_KEY)
    if cached_data:
        book_dicts = json.loads(cached_data)
        return [Book(**b) for b in book_dicts]
    return None

def cache_books(books: List[Book]):
    if not redis_available:
        return
    books_json = json.dumps([book.dict() for book in books])
    redis_client.set(BOOK_CACHE_KEY, books_json, ex=60)  # 60 seconds expiration
