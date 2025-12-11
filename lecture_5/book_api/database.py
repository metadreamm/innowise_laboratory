from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# A file named 'books.db' in the current directory
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

# create_engine is the core component that establishes connectivity to the database
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# sessionmaker creates a Session class bound to this engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative_base is used to define all ORM classes
Base = declarative_base()

# Define the Book ORM Model
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=True)  #optional

# Create the database table (if it doesn't exist)
def create_db_tables():
    Base.metadata.create_all(bind=engine)