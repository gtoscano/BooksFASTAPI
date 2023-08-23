from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, Sequence('book_id_seq'), primary_key=True)
    author = Column(String)
    title = Column(String)
    year = Column(Integer, nullable=True)

DATABASE_URL = "postgresql://username:yourpassword@localhost:5432/bookdb"
engine = create_engine(DATABASE_URL)

if __name__ == "__main__":
    # Create the table
    Base.metadata.create_all(engine)
    print("Tables created successfully!")

