
from os import getenv

from elasticsearch_dsl import Document, Text, Keyword


class AnnotatorElastic(Document):

    text = Text(analyzer="snowball")
    id = Text()
    chunk = Text(fields={"raw": Keyword()})

    class Index:

        name = "annotator"
        settings = {"number_of_shards": 2}
