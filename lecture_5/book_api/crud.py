from sqlalchemy.orm import Session
import database, schemas

# Function to CREATE a new book (POST /books/)
def create_book(db: Session, book: schemas.BookCreate):
    db_book = database.Book(**book.model_dump())        # dict() is deprecated
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Function to READ all books (GET /books/)
def get_books(db: Session):
    return db.query(database.Book).all()

# Function to READ a single book by ID
def get_book_by_id(db: Session, book_id: int):
    return db.query(database.Book).filter(database.Book.id == book_id).first()

# Function to DELETE a book (DELETE /books/{book_id})
def delete_book(db: Session, book_id: int):
    db_book = get_book_by_id(db, book_id)
    if db_book:
        db.delete(db_book)
        db.commit()
        return db_book
    return None

# Function to UPDATE book details (PUT /books/{book_id})
def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    db_book = get_book_by_id(db, book_id)
    if db_book:
        # Update attributes from the Pydantic model
        for key, value in book.dict(exclude_unset=True).items():
            setattr(db_book, key, value)
        
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book
    return None

# Function to SEARCH books (GET /books/search/)
def search_books(db: Session, query: str):
    search_pattern = f"%{query}%"
    
    # Query for matches in title, author, OR year
    return db.query(database.Book).filter(
        (database.Book.title.ilike(search_pattern)) | 
        (database.Book.author.ilike(search_pattern)) | 
        (database.Book.year.cast(database.String).ilike(search_pattern)) # Cast year to string for searching
    ).all()