# Elastic Search is been used as
# search engine.
from json import loads

from elasticsearch_dsl import connections

from pntl.utils import env_json


def connect():

    connections.create_connection(**env_json("ELASTICSEARCH_HOST"))
