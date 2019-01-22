export DEBUG=true
export DEFAULT_LEN=400
export POS_LEN=400
export NER_LEN=400
export DEP_LEN=400
export SRL_LEN=400
export CHUNK_LEN=400
export VERB_LEN=400
export HASH_VALUE_LEN=10
export DATABASE_ECHO=${DEBUG}
export DATABASE_URL=postgresql:///pntlTest
export TABLENAME=package_items

export REDISH_HOST=redis://127.0.0.1:6379/1 #optional
# use bonsai.com for creating elastic search if you don't have it.
export ELASTICSEARCH_HOST='{"hosts":["localhost"], "verify_certs": true}'
export DB_CLASS=pntl.db.model.ElasticPackage
export HASH_CLASS=hashlib.md5