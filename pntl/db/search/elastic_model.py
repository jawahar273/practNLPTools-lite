from elasticsearch_dsl import Document, Text, Keyword
from elasticsearch_dsl.exceptions import ElasticsearchDslException


class AnotatorElasticException(ElasticsearchDslException):
    pass


class DuplicateAnomalyElastic(AnotatorElasticException):
    pass


class AnnotatorElastic(Document):

    words = Text()
    verbs = Text(fields={"raw": Keyword()})

    class Index:

        name = "annotator"
        settings = {"number_of_shards": 2}
