
from elasticsearch_dsl import Document, Text, Keyword


class AnnotatorElastic(Document):

    id = Text()
    text = Text(analyzer="snowball")
    chunk = Text(fields={"raw": Keyword()})

    class Index:

        name = "annotator"
        # settings = {"number_of_shards": 2}
