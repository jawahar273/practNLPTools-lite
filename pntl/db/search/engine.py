
from pntl.db.search.abstract import AbstractEngine
from pntl.db.search import config

from pntl.db.search.elastic import AnnotatorElastic

from pntl.db.search import config


# Init the connection for Elastic Search engine.
config.connect()

# Mapping the Elastic Search persistance storage.
AnnotatorElastic().init()


class ElasticEngine(AbstractEngine):
    """docstring for SearchEngine"""

    def __init__(self, **kwargs):

        temp = AnnotatorElastic(**kwargs)
        temp.save()

        return True
