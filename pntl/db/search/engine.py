
from pntl.db.search.abstract import AbstractEngine
from pntl.db.search import config

from pntl.db.search.elastic import AnnotatorElastic


class ElasticEngine(AbstractEngine):
    """docstring for SearchEngine"""

    def __init__(self, arg):
        AnnotatorElastic().init()

    def insert(self, **kwargs):

        temp = AnnotatorElastic(**kwargs)
        temp.save()

        return True
