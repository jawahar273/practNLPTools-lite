""" Database class are declare in the file.
"""
from os import getenv

from sqlalchemy import Column, Integer, String, UnicodeText

from pntl.db.config import Base
from pntl.db.json_field import JSONEncodedDict

from pntl.utils import pntl_hash, env_int


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

    words = Column(UnicodeText())
    syntax_tree = Column(UnicodeText())
    pos = Column(_json_field(env_int("POS_LEN")))
    ner = Column(_json_field(env_int("NER_LEN")))
    dep_parse = Column(_json_field(env_int("DEP_LEN")), nullable=True)
    srl = Column(_json_field(env_int("SRL_LEN")))
    chunk = Column(_json_field(env_int("CHUNK_LEN")))
    verbs = Column(_json_field(env_int("VERB_LEN")))
    hash_str = Column(String(env_int("HASH_VALUE_LEN", 20)), unique=True)

    def __init__(self, words, syntax_tree, pos, ner, dep_parse, srl, chunk, verbs):

        self.words = words
        self.syntax_tree = syntax_tree
        self.pos = pos
        self.ner = ner
        self.dep_parse = dep_parse
        self.srl = srl
        self.chunk = chunk
        self.verbs = verbs
        self.hash_str = pntl_hash(words)
