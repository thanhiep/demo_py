from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from . import models

URL_DATABASE = 'mysql+pymysql://root:123456@localhost:3307/db_pinterest'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

models.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()