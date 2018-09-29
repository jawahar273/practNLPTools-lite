# Elastic Search is been used as
# search engine.
from json import loads

from elasticsearch_dsl import connections
from pntl.utils import env_str


def connect():

    connections.create_connection(**loads(env_str("ELASTICSEARCH_HOST")))
