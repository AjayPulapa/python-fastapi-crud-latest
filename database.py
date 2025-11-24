"""
database.py
-----------
Creates the MySQL database engine and session.
This is shared between ORM (employees) and RAW SQL (orders).
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# load_dotenv()

# # Load environment variables (dynamic for Docker & Local)
# DB_USER = os.getenv("DB_USER", "root")
# DB_PASS = os.getenv("DB_PASS", "password")
# DB_HOST = os.getenv("DB_HOST", "localhost")
# DB_PORT = os.getenv("DB_PORT", "3306")    # ✅ DB PORT INCLUDED
# DB_NAME = os.getenv("DB_NAME", "testdb")


DB_USER="root"
DB_PASS="root"
DB_HOST="localhost"
DB_NAME="fastapidb"
DB_PORT="3306"


# Build the correct MySQL connection URL
DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)   # ✅ PORT ADDED HERE

# Initialize SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create session
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Dependency function for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
