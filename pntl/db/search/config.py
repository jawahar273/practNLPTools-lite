# Elastic Search is been used as
# search engine.
from os import getenv

from elasticsearch_dsl import connections

connections.configure(**dict(getenv("")))
