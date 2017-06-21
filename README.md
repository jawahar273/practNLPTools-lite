# practNLPTools-lite
Creating practNLPTools in lite mode.

![Author](https://img.shields.io/badge/Author-jawahar-blue.svg)
![Python-version](https://img.shields.io/badge/Python%20Version-Python--2.7-red.svg) 
![Python-version](https://img.shields.io/badge/from-to-yellowgreen.svg) 
![Python-version](https://img.shields.io/badge/Python%20Version-Python--3.5-green.svg)

[![Build Status](https://travis-ci.org/jawahar273/practNLPTools.svg?branch=master)](https://travis-ci.org/jawahar273/practNLPTools) - on click this built this might take you to build of [practNLPTools](https://github.com/jawahar273/practNLPTools) which is testing ground for this repository so don't worry.

Practical Natural Language Processing Tools for Humans.<br>
practNLPTools is a pythonic library over [SENNA](http://ronan.collobert.com/senna/) and Stanford Dependency Extractor.



Functionality
=============
* Semantic Role Labeling
* Syntactic Parsing
* Part of Speech Tagging (POS Tagging)
* Named Entity Recognisation (NER)
* Dependency Parsing
* Shallow Chunking
* Skip-gram(in-case)

Future work
==========
* ~~automatic takes senna path if it install in system~~
* copying stanford parser and depPaser file into installed direction
* creating depParser for corresponding os environment
* custome input format for stanford parser insted of tree format

Features
=============
1. Fast: [SENNA](http://ronan.collobert.com/senna/) is written is C. So it is Fast.
2. We use only dependency Extractor Component of Stanford Parser, which takes in Syntactic Parse from SENNA and applies dependency Extraction. So there is no need to load parsing models for Stanford Parser, which takes time.
3. Easy to use.
4. Platform Supported - Windows, Linux and Mac

>Notes:
  SENNA pipeline has a fixed maximum size of the sentences that it can read.
    By default it is 1024 token/sentence. If you have larger sentences, changing
    the MAX_SENTENCE_SIZE value in SENNA_main.c should be considered and your
    system specific binary should be rebuilt. Otherwise this could introduce
    misalignment errors.
    
Installation
=============

Requires:
A computer with 500mb memory, Java Runtime Environment (1.7 preferably, works with 1.6 too, but didnt test.) installed and python.

If you are in linux:
run:
```
sudo python setup.py install 
```
If you are in windows:
run this commands as administrator:

```
python setup.py install
``` 

Bench Mark comparsion
=====================
By using the `time` command in ubuntu on running the `testsrl.py` on this [link](https://github.com/jawahar273/SRLTagger) and along with `tools.py` on `pntl`  

|      | pntl | NLTK-senna |
| --   | --   | ---  |
| at fist run |   |   |
|      |real	0m1.674s | real	0m2.484s
|      |user	0m1.564s | user	0m1.868s
|      |sys	0m0.228s | sys	0m0.524s
| at second run |     |
|      | real	0m1.245s | real	0m3.359s
|      | user	0m1.560s | user	0m2.016s
|      | sys	0m0.152s   | sys	0m1.168s

> note: this bench mark may differt accouding to system's working and to restult present here is exact same result in my system 
ububtu 4Gb RAM and i3 process. If I find another good benchmark techinque then I will change to it. 


Dependency 
=====================
* Sphinx 1.5+ [only need it for building doc html]

```
cd api
make html
```
The about command is used to generate html from docstring

Visulize
=========
* [conllu](https://github.com/EmilStenstrom/conllu) (To make visulize possible with only CoNLLU format) 
