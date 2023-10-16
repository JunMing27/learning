#
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#this credential is just for testing 
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:abcd1234@localhost/fastapi"

# engine is smtg that build the connection between the sqlalchemy and postgres
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#session is to communicate with the postgres
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#tables that would be created will be extending the base class
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()