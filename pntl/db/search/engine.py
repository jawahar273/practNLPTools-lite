from elasticsearch_dsl import Search

from pntl.db.search.abstract import AbstractEngine
from pntl.db.search import config

from pntl.db.search.elastic_model import AnnotatorElastic

from pntl.db.search import config


# Init the connection for Elastic Search engine.
config.connect()

# Mapping the Elastic Search persistance storage.
AnnotatorElastic().init()


class ElasticEngine(AbstractEngine):
    def __init__(self, kwargs):
        """
        Insert into the elastic server and return
        `True` if success.
        """
        self.elastic = AnnotatorElastic(**kwargs)
        self.save(self.elastic.words)

    @classmethod
    def save(cls, search_text):
        """
        Save function make a request to the elastic server
        and making custom check constrain on the server.

        .. warning::
            Through on the saving to the server we are avoding
            duplicate but this is not a case if the server is
            update out-of-scope(mannully through admin like wise).
        """
        # quick ref: using async/concurrent concept for speeding
        # the process

        response = cls.query(search_text, matching_type="match", status=True)

        if response:
            return AnnotatorElastic.save()

        return

    @classmethod
    def detectDuplicate(cls, hits):
        """
        Check the hits is empty if then return `False`
        as it has no duplicate.
        """
        hits_count = len(hits)

        if not hits:
            return False

        return hits_count > 1

    @classmethod
    def query(cls, search_words, matching_type="match", status=False):
        """
        Calling query which is used for fetching the result from the
        server.

        :param str search_words: sentence to be searched in the elastic
        server.
        :param str matching_type: match the given sentence base the
        type.
        :param bool status: return `bool` to see if the response is
        success and also it has a `hits`
        :return: return the `Response` object based on `param:` status .

        """
        result = AnnotatorElastic.search().query(matching_type, words=search_words)
        response = result.execute()
        if status:
            return response.success() and not response.hits

        return response
