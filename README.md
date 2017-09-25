# practNLPTools-lite
Creating practNLPTools in lite mode.

![Author](https://img.shields.io/badge/Author-jawahar-blue.svg)
![Python-version](https://img.shields.io/badge/Python%20Version-Python--2.7-red.svg) 
![Python-version](https://img.shields.io/badge/from-to-yellowgreen.svg) 
![Python-version](https://img.shields.io/badge/Python%20Version-Python--3.5-green.svg)

[![Build Status](https://travis-ci.org/jawahar273/practNLPTools.svg?branch=master)](https://travis-ci.org/jawahar273/practNLPTools) - on click this built this might take you to build of [practNLPTools](https://github.com/jawahar273/practNLPTools) which is testing ground for this repository so don't worry.

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Fjawahar273%2FpractNLPTools-lite.svg?type=small)](https://app.fossa.io/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Fjawahar273%2FpractNLPTools-lite?ref=badge_small)

Practical Natural Language Processing Tools for Humans.<br>
practNLPTools is a pythonic library over [SENNA](http://ronan.collobert.com/senna/) and Stanford Dependency Extractor.



# Functionality

* Semantic Role Labeling
* Syntactic Parsing
* Part of Speech Tagging (POS Tagging)
* Named Entity Recognisation (NER)
* Dependency Parsing
* Shallow Chunking
* Skip-gram(in-case)

# Future work

* ~~automatic takes senna path if it install in system~~
* copying stanford parser and depPaser file into installed direction
* creating depParser for corresponding os environment
* custome input format for stanford parser insted of tree format

# Features

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
    
# Installation


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

<h1>Bench Mark comparsion</h1>
<p>By using the <code>time</code> command in ubuntu on running the <code>testsrl.py</code> on this <a href="https://github.com/jawahar273/SRLTagger">link</a> and along with <code>tools.py</code> on <code>pntl</code></p>
<table>
	<thead>
		<tr>
			<th></th>
			<th>pntl</th>
			<th>NLTK-senna</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>at fist run</td>
			<td></td>
			<td></td>
		</tr>

		<tr>
			<td></td>
			<td>real	0m1.674s</td>
			<td>real	0m2.484s</td>
		</tr>

		<tr>
			<td></td>
			<td>user	0m1.564s</td>
			<td>user	0m1.868s</td>
		</tr>

		<tr>
			<td></td>
			<td>sys	0m0.228s</td>
			<td>sys	0m0.524s</td>
		</tr>

		<tr>
			<td>at second run</td>
			<td></td>
			<td></td>
		</tr>

<tr>
<td></td>
<td>real	0m1.245s</td>
<td>real	0m3.359s</td>
</tr>
<tr>
<td></td>
<td>user	0m1.560s</td>
<td>user	0m2.016s</td>
</tr>
<tr>
<td></td>
<td>sys	0m0.152s</td>
<td>sys	0m1.168s</td>
</tr></tbody></table>

<div>
 note: this bench mark may differt accouding to system's working and to restult present here is exact same result in my system 
ububtu 4Gb RAM and i3 process. If I find another good benchmark techinque then I will change to it. 
</div>

# Dependency 

* Sphinx 1.5+ [only need it for building doc html]

```
cd api
make html
```
The about command is used to generate html from docstring

# Visulize

* [conllu](https://github.com/EmilStenstrom/conllu) (To make visulize possible with only CoNLLU format) 


