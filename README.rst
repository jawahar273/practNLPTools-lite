==================
practNLPTools-lite
==================

Creating practNLPTools in lite mode.[ get the old coding in `devbranch`_  or previous stable  `properbranch`_ ]

|Author|

|Build Status| - on click this built this might take you to build of
`practNLPTools`_ which is testing ground for this repository so don’t
worry.


Practical Natural Language Processing Tools for Humans.
practNLPTools is a pythonic library over `SENNA`_ and Stanford
Dependency Extractor.

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

.. |Wercker status| image:: https://app.wercker.com/status/758bf4fa0e3bb9066d118385ee4aac1f/s/master
   :target: https://app.wercker.com/project/byKey/758bf4fa0e3bb9066d118385ee4aac1f

+-----------------+-----------------+
|    name         | status          |
+=================+=================+
| Wercker status  | |Wercker status||
+-----------------+-----------------+
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

* Documentation: https://pntl.readthedocs.io

QuickStart 
==========

Downlarding Stanford Parser JAR
###############################

To downlard the stanford-parser from github automatically and placing them inside the install direction.

.. code:: bash

   pntl -I true
   # downlards required file from github.

Running Predefine Examples Sentences
#####################################

To run exiting example for batch(which has more than one list of examples).

.. code:: bash

   pntl -SE home/user/senna -B true

To run predefine example for one sentence.

.. code:: bash

   pntl -SE home/user/senna

Running user given sentence
###########################

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

Requires:
~~~~~~~~~
  A computer with 500mb memory, Java Runtime Environment (1.7
  preferably, works with 1.6 too, but didnt test.) installed and python.

Linux:
```````
run:

::

    sudo python setup.py install 

windows:
````````
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

   this bench mark may differt accouding to system’s working and to restult present here is exact same result in my system ububtu 4Gb RAM
   and i3 process. If I find another good benchmark techinque then I will
   change to it.


.. _practNLPTools: https://github.com/jawahar273/practNLPTools-lite
.. _SENNA: http://ronan.collobert.com/senna/
.. _properbranch: https://github.com/jawahar273/practNLPTools-lite/tree/pyup-update-pytest-3.2.2-to-3.2.3
.. _devbranch: https://github.com/jawahar273/practNLPTools-lite/tree/dev

.. |Author| image:: https://img.shields.io/badge/Author-jawahar-blue.svg
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
