import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# use of the engine
engine = create_engine(os.getenv('DATABASE_URL', 'postgres:///'))

# global session
SessionMaker = sessionmaker(bind=engine)

# base of the class DB
Base = declarative_base()