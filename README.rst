==================
practNLPTools-lite
==================

This project is a fork of `biplab-iitb`_

.. _biplab-iitb: https://github.com/biplab-iitb/practNLPTools

.. warning::
  
    CLI is only for example purpose don't use for long running jobs.

Get the very old code in `devbranch`_  or prior stable version `oldVersion`_.

|Author| |python_version| |HitCount|

|Build Status| - this built might take you to
`practNLPTools`_ which is testing ground for this repository so don’t
worry.


Practical Natural Language Processing Tools for Humans.
practNLPTools is a pythonic library over `SENNA`_ and Stanford
Dependency Extractor.


.. |HitCount| image:: http://hits.dwyl.io/jawahar273/practNLPTools-lite.svg
   :target: http://hits.dwyl.io/jawahar273/practNLPTools-lite

.. |pypi status| image:: https://img.shields.io/pypi/v/practNLPTools-lite.svg
        :target: https://pypi.python.org/pypi/pntl

.. |travis status| image:: https://img.shields.io/travis/jawahar273/practNLPTools-lite.svg
        :target: https://travis-ci.org/jawahar273/practNLPTools-lite

.. |doc status| image:: https://readthedocs.org/projects/pntl/badge/?version=latest
        :target: https://pntl.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. |dep status| image:: https://pyup.io/repos/github/jawahar273/practNLPTools-lite/shield.svg
     :target: https://pyup.io/repos/github/jawahar273/practNLPTools-lite/
     :alt: Updates

.. |blocker status| image:: https://pyup.io/repos/github/jawahar273/practNLPTools-lite/python-3-shield.svg
     :target: https://pyup.io/repos/github/jawahar273/practNLPTools-lite/
     :alt: Python 3

+-----------------+-----------------+
|    name         | status          |
+=================+=================+
| PyPi            |    |pypi status||
+-----------------+-----------------+
| travis          |  |travis status||
+-----------------+-----------------+
| Documentation   |     |doc status||
+-----------------+-----------------+
| dependency      |     |dep status||
+-----------------+-----------------+
| blocker Pyupbot | |blocker status||
+-----------------+-----------------+
| FOSSA           |   |FOSSA Status||
+-----------------+-----------------+

* Documentation `docs1`_ and `docs2`_

.. _docs1: https://pntl.readthedocs.io
.. _docs2:  https://htmlpreview.github.io/?https://raw.githubusercontent.com/jawahar273/practNLPTools-lite/master/docs/index.html

.. note::
  After version 0.3.0+ pntl should able to store the result into
  database for later usage if needed by installing below dependency.

  `pip install git+https://github.com/jawahar273/snowbase.git`


QuickStart 
==========

Downlarding Stanford Parser JAR
===============================

To downlard the stanford-parser from github automatically and placing them inside the install direction.

.. code:: bash

   pntl -I true
   # downlards required file from github.

Running Predefine Examples Sentences
=======================================

To run predefine example in batch mode(which has more than one list of examples).

.. code:: bash

   pntl -SE home/user/senna -B true

Example
-------

Batch mode means listed sentences.

..code:: 

    # Example structure for predefine
    # Sentences in the code.

    sentences = [
        "This is line 1",
        "This is line 2",

    ]

To run predefine example in non batch mode.

.. code:: bash

   pntl -SE home/user/senna

Running user given sentence
===========================

To run user given example using `-S` is

.. code:: bash

   pntl -SE home/user/senna -S 'I am gonna make him an offer he can not refuse.'


Functionality
=============

-  Semantic Role Labeling.
-  Syntactic Parsing.
-  Part of Speech Tagging (POS Tagging).
-  Named Entity Recognisation (NER).
-  Dependency Parsing.
-  Shallow Chunking.
-  Skip-gram(in-case).
-  find the senna path if is install in the system.
-  stanford parser and depPaser file into installed direction.

Future work
===========
-  tag2file(new)
-  creating depParser for corresponding os environment
-  custome input format for stanford parser insted of tree format


Features
========

#. Fast: `SENNA`_ is written is C. So it is Fast.
#. We use only dependency Extractor Component of Stanford Parser, which
   takes in Syntactic Parse from SENNA and applies dependency
   Extraction. So there is no need to load parsing models for Stanford
   Parser, which takes time.
#. Easy to use.
#. Platform Supported - Windows, Linux and Mac
#. Automatic finds stanford parsing jar if it is present in install path[pntl].

.. note::
    
    SENNA pipeline has a fixed maximum size of the sentences that it
    can read. By default it is 1024 token/sentence. If you have larger
    sentences, changing the MAX\_SENTENCE\_SIZE value in SENNA\_main.c should beconsidered and your system specific binary should be rebuilt. Otherwise this could introduce misalignment errors.

Installation
============

**Requires:**

    A computer with 500mb memory, Java Runtime Environment (1.7
    preferably, works with 1.6 too, but didnt test.) installed and python.

    **Linux:**

    run:

    ::

        sudo python setup.py install 

    windows:

    run this commands as administrator:

    ::

        python setup.py install


Bench Mark comparsion
=====================

By using the ``time`` command in ubuntu on running the ``testsrl.py`` on
this `link`_ and along with ``tools.py`` on ``pntl``

.. _link: https://github.com/jawahar273/SRLTagger


+-----------------+-----------------+-----------------+
|                 | pntl            | NLTK-senna      |
+=================+=================+=================+
| at fist run     |                 |                 |
+-----------------+-----------------+-----------------+
|                 | real 0m1.674s   | real 0m2.484s   |
+-----------------+-----------------+-----------------+
|                 | user 0m1.564s   | user 0m1.868s   |
+-----------------+-----------------+-----------------+
|                 | sys 0m0.228s    | sys 0m0.524s    |
+-----------------+-----------------+-----------------+
| at second run   |                 |                 |
+-----------------+-----------------+-----------------+
|                 | real 0m1.245s   | real 0m3.359s   |
+-----------------+-----------------+-----------------+
|                 | user 0m1.560s   | user 0m2.016s   |
+-----------------+-----------------+-----------------+
|                 | sys 0m0.152s    | sys 0m1.168s    |
+-----------------+-----------------+-----------------+


.. note:: 

   This benchmark may diffrent from system to sytem. The result produced here is from ububtu 4Gb RAM
   and i3 process.

.. _practNLPTools: https://github.com/jawahar273/practNLPTools-lite
.. _SENNA: http://ronan.collobert.com/senna/
.. _oldVersion: https://github.com/jawahar273/practNLPTools-lite/tree/pyup-update-pytest-3.2.2-to-3.2.3
.. _devbranch: https://github.com/jawahar273/practNLPTools-lite/tree/dev

.. |Author| image:: https://img.shields.io/badge/Author-jawahar-blue.svg
.. |python_version| image:: https://img.shields.io/badge/python3+-only-red.svg
.. |Python-version-3| image:: https://img.shields.io/badge/Py-version-Python--3.5-green.svg
.. |Build Status| image:: https://travis-ci.org/jawahar273/practNLPTools.svg?branch=master
   :target: https://travis-ci.org/jawahar273/practNLPTools
.. |FOSSA Status| image:: https://app.fossa.io/api/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Fjawahar273%2FpractNLPTools-lite.svg?type=small
   :target: https://app.fossa.io/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Fjawahar273%2FpractNLPTools-lite?ref=badge_small


.. Features
.. --------

.. * TODO

Credits
=======

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
