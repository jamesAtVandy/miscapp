from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

password = "" #placeholder
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:{password}@localhost:5432/jrbuysDB"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
