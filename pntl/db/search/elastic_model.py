from elasticsearch_dsl import Document, Text, Keyword


class AnnotatorElastic(Document):

    words = Text()
    verbs = Text(fields={"raw": Keyword()})

    class Index:

        name = "annotator"
        settings = {"number_of_shards": 2}
