''' Database class are declare in the file.
'''
import os

from sqlalchemy import Column, Integer, String, UnicodeText

from pntl.db.config import Base
from pntl.db.json_field import JSONEncodedDict

from pntl.utils import to_int


class Package(Base):

    __tablename__ = os.getenv('TABLENAME', 'content')

    id = Column(Integer, primary_key=True)

    text = Column(UnicodeText())
    syntax_tree = Column(UnicodeText())
    pos = Column(JSONEncodedDict(to_int(os.getenv('POS_LEN'))))
    ner = Column(JSONEncodedDict(to_int(os.getenv('NER_LEN'))))
    dep = Column(JSONEncodedDict(to_int(os.getenv('DEP_LEN'))))
    srl = Column(JSONEncodedDict(to_int(os.getenv('SRL_LEN'))))
    chunk = Column(JSONEncodedDict(to_int(os.getenv('CHUNK_LEN'))))
