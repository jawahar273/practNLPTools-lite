API
=====
A general interface of the SENNA and Stanford Dependency
Extractor pipeline that supports any of
the operations specified in SUPPORTED_OPERATIONS.
SUPPORTED_OPERATIONS: It provides
Part of Speech Tags, Semantic Role Labels, Shallow Parsing (Chunking),
Named Entity Recognisation (NER), Dependency Parse and
Syntactic Constituency Parse.
Applying multiple operations at once has the speed advantage. For example,
senna v3.0 will calculate the POS tags in case you are extracting the named
entities. Applying both of the operations will cost only the time of
extracting the named entities. Same is true for dependency Parsing.
SENNA pipeline has a fixed maximum size of the sentences that it can read.
By default it is 1024 token/sentence. If you have larger sentences,
changing
the MAX_SENTENCE_SIZE value in SENNA_main.c should be considered and your
system specific binary should be rebuilt. Otherwise this could introduce
misalignment errors
and for Dependency Parser the requirement is Java Runtime Environment :)

.. autoclass:: pntl.tools.Annotator
   :members:



.. autofunction:: pntl.tools.test

.. autofunction:: pntl.cli.user_test
