""" Database class are declare in the file.
    :py:class:`Package` is simple class for only used in
    accessing and storing the result of the output value.
    By using the hash string the result can be easly access
    with out must computing power rather leading database engine
    searching for as. In worst case the db engine has to look
    up on the all the row for matching or the sentence might
    be realy long which inter must of its time.

    .. note::
        Users can customise the default behaviour using user
        define class in changing inserting the class in `DB_CLASS`.
 
    :py:class:`ElasticPackage`  is still under construction as
    it planning to intergate with elastic search engine which
    intern increase the searching 2x speed(only theroy).
"""

from sqlalchemy import Column, Integer, String, UnicodeText
from sqlalchemy.exc import SQLAlchemyError

from pntl.db.config import Base
from pntl.db.json_field import JSONEncodedDict

from pntl.db.utils import pntl_hash, env_int, env_str
from pntl.db.search.engine import ElasticEngine


def _json_field(value):
    """Just a proxy name for the :py:class:JSONEncodedDict

    [description]
    :param value: len the field(for now)
    :type value: str
    :returns: instance of :py:class:JSONEncodedDict
    :rtype: :py:class:JSONEncodedDict
    """
    return JSONEncodedDict(value)


class DuplicateAnomaly(SQLAlchemyError):
    """
    Rasie when there is duplicate entry (or) anomaly in
    the database. This exception is just a way to make
    some adjustment for out-of-box write to database.
    """

    def __init__(self, *arg, **kw):

        super().__init__(
            self, f"Duplicate anomaly(or)entry has been detected \n {kw.get('msg')}"
        )


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
    hash_str = Column(String(env_int("HASH_VALUE_LEN", default=20)), unique=True)


class Package(AbstractPackage):

    __tablename__ = env_str("TABLENAME", default="simple_db")

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

    @classmethod
    def filter(cls, search_text):
        """
        Find the hash value of the given sentence.
        """
        return pntl_hash(search_text)


class ElasticPackage(AbstractPackage):

    __tablename__ = env_str("TABLENAME", "elastic_db")

    def __init__(self, words, syntax_tree, pos, ner, dep_parse, srl, chunk, verbs):
        """
        In using this class the result will be saved into the database
        and the result will be saved in elastic search engine.
        """
        self.words = words
        self.syntax_tree = syntax_tree
        self.pos = pos
        self.ner = ner
        self.dep_parse = dep_parse
        self.srl = srl
        self.chunk = chunk
        self.verbs = verbs
        self.hash_str = pntl_hash(words)

        self.save_elastic({"words": self.words, "verbs": self.verbs})

    @classmethod
    def save_elastic(cls, kw):
        """
        Calling on each time if there is inserting value
        into the db.
        .. warning::
        This work flow don't detect duplicate.
        """

        ElasticEngine(kw)

    @classmethod
    def filter(cls, search_text):
        """
        Search method is used for searching the elastic server
        for the given `sentence` and then it is passed to the db
        to fetch the details result.
        """

        response = ElasticEngine.query(search_text, "match")
        # quick ref: must uncomment
        # if ElasticEngine.detectDuplicate(response.hits):
        #     raise DuplicateAnomaly(msg="May be Out-of-box write into the server")

        # quick ref: need some kind of warning system if the lenght
        # of the `hits` more than one.
        return pntl_hash(response[0].words)
