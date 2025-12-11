from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import database, schemas, crud

# Initialize the app
app = FastAPI()

database.create_db_tables()

# Get a database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Check if the API is running
@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Collection API!"}

# POST /books/ : Add a new book (CREATE)
@app.post("/books/", response_model=schemas.Book)
def create_new_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)

# GET /books/ : Get all books (READ)
@app.get("/books/", response_model=List[schemas.Book])
def read_all_books(db: Session = Depends(get_db)):
    return crud.get_books(db=db)

# DELETE /books/{book_id} : Delete a book by ID (DELETE)
@app.delete("/books/{book_id}", status_code=204) # HTTP 204 No Content on successful deletion
def delete_book_by_id(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.delete_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return 

# PUT /books/{book_id} : Update book details (UPDATE)
@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book_details(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.update_book(db=db, book_id=book_id, book=book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

# GET /books/search/ : Search books by title, author, or year (SEARCH)
# a query parameter 'q' for the search term
@app.get("/books/search/", response_model=List[schemas.Book])
def search_book_collection(q: str, db: Session = Depends(get_db)):
    if not q:
        raise HTTPException(status_code=400, detail="Search query 'q' must be provided.")
    return crud.search_books(db=db, query=q)