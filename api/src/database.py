from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(
    "sqlite:///./database.db", connect_args={"check_same_thread": False}
)

session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autocommit=False,
)


def get_session():
    db = session()
    try:
        yield db
        db.commit()
    finally:
        db.close()


def get_db_graphql():
    db = session()
    try:
        return db
    finally:
        db.close()


Base = declarative_base()
