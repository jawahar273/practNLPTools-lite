''' Database class are declare in the file.
'''
import os

from sqlalchemy import Column, Integer, String, UnicodeText

from pntl.db.config import Base
from pntl.db.json_field import JSONEncodedDict

from pntl.utils import to_int

def _json_field(value):

    return JSONEncodedDict(value)

class Package(Base):

    __tablename__ = os.getenv('TABLENAME', 'content')

    id = Column(Integer, primary_key=True)

    text = Column(UnicodeText())
    syntax_tree = Column(UnicodeText())
    pos = Column(_json_field(to_int(os.getenv('POS_LEN'))))
    ner = Column(_json_field(to_int(os.getenv('NER_LEN'))))
    dep_parse = Column(_json_field(to_int(os.getenv('DEP_LEN'))), nullable=True)
    srl = Column(_json_field(to_int(os.getenv('SRL_LEN'))))
    chunk = Column(_json_field(to_int(os.getenv('CHUNK_LEN'))))
    verb = Column(_json_field(to_int(os.getenv('SRL_LEN'))))
