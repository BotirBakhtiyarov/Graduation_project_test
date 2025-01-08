from sqlalchemy import create_engine, Column, String, Integer, Text, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize the base
Base = declarative_base()

# Define the Literature model
class Literature(Base):
    __tablename__ = 'literature'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    authors = Column(String, nullable=False)
    publication_date = Column(String)
    location = Column(String)
    abstract = Column(Text)
    summary = Column(Text)
    outline = Column(Text)
    file_path = Column(String, nullable=False)

# Create the engine and session
engine = create_engine('sqlite:///database.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

# Initialize the database by running this once
if __name__ == "__main__":
    init_db()