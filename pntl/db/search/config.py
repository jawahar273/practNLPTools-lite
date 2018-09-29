# Elastic Search is been used as
# search engine.
from os import getenv
from json import loads

from elasticsearch_dsl import connections


def connect():

    connections.create_connection(**loads(getenv("ELASTICSEARCH_HOST")))
