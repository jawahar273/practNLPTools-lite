""" Database class are declare in the file.
    :py:class:`Package` is simple class for only used in
    accessing and storing the result of the output value.
    By using the hash string the result can be easly access
    with out must computing power rather leading database engine
    searching for as. In worst case the db engine has to look
    up on the all the row for matching or the sentence might
    be realy long which inter must of its time.
    :py:class:`ElasticPackage` is still under construction as
    it planning to intergate with elastic search engine which
    intern increase the searching 2x speed(only theroy).
"""

from sqlalchemy import Column, Integer, String, UnicodeText

from pntl.db.config import Base
from pntl.db.json_field import JSONEncodedDict
from pntl.db.search.engine import ElasticEngine

from pntl.utils import pntl_hash, env_int, env_str


def _json_field(value):
    """Just a proxy name for the :py:class:JSONEncodedDict

    [description]
    :param value: len the field(for now)
    :type value: str
    :returns: instance of :py:class:JSONEncodedDict
    :rtype: :py:class:JSONEncodedDict
    """
    return JSONEncodedDict(value)


class AbstractPackage(Base):

    __abstract__ = True
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    words = Column(UnicodeText())
    syntax_tree = Column(UnicodeText())
    pos = Column(_json_field(env_int("POS_LEN")))
    ner = Column(_json_field(env_int("NER_LEN")))
    dep_parse = Column(_json_field(env_int("DEP_LEN")), nullable=True)
    srl = Column(_json_field(env_int("SRL_LEN")))
    chunk = Column(_json_field(env_int("CHUNK_LEN")))
    verbs = Column(_json_field(env_int("VERB_LEN")))


class Package(AbstractPackage):

    __tablename__ = env_str("TABLENAME", default="same_pc")

    hash_str = Column(String(env_int("HASH_VALUE_LEN", default=20)), unique=True)

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


class ElasticPackage(AbstractPackage):

    __tablename__ = env_str("TABLENAME", "dist")
