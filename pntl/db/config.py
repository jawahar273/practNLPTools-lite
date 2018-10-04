
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from pntl.utils import env_str, env_bool


# use of the engine
engine = create_engine(
    env_str("DATABASE_URL", "postgres:///"), echo=env_bool("DATABASE_ECHO", False)
)

# global session
SessionMaker = sessionmaker(bind=engine, autoflush=False)

# base of the class DB
Base = declarative_base()
