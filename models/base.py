import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'sqlite:///{0}/trello_workon.db'.format(os.getcwd()),
    convert_unicode=True,
)

db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )
)

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    from models import (
        user
    )
    Base.metadata.create_all(bind=engine)

def reset_db():
    from models import (
        user
    )
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)