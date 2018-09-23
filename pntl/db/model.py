""" Database class are declare in the file.
"""
from os import getenv

from sqlalchemy import Column, Integer, String, UnicodeText

from pntl.db.config import Base
from pntl.db.json_field import JSONEncodedDict

from pntl.utils import to_int


def _json_field(value):
    """Just a proxy name for the :py:class:JSONEncodedDict

    [description]
    :param value: len the field(for now)
    :type value: str
    :returns: instance of :py:class:JSONEncodedDict
    :rtype: :py:class:JSONEncodedDict
    """
    return JSONEncodedDict(value)


class Package(Base):

    __tablename__ = getenv("TABLENAME", "content")

    id = Column(Integer, primary_key=True)

    text = Column(UnicodeText())
    syntax_tree = Column(UnicodeText())
    pos = Column(_json_field(to_int(getenv("POS_LEN"))))
    ner = Column(_json_field(to_int(getenv("NER_LEN"))))
    dep_parse = Column(_json_field(to_int(getenv("DEP_LEN"))), nullable=True)
    srl = Column(_json_field(to_int(getenv("SRL_LEN"))))
    chunk = Column(_json_field(to_int(getenv("CHUNK_LEN"))))
    verb = Column(_json_field(to_int(getenv("VERB_LEN"))))
