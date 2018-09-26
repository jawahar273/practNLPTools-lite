
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from pntl.utils import env_bool, env_str

# use of the engine
engine = create_engine(
    env_str("DATABASE_URL", "postgres:///"), echo=env_bool("DATABASE_ECHO", True)
)

# global session
SessionMaker = sessionmaker(bind=engine)

# base of the class DB
Base = declarative_base()
