from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv(".env")
SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
