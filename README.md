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
* automatic takes senna path if it install in system
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

| pntl | NLTK-senna |
| --   | ---  |
| at fist run 
|real	0m1.674s | real	0m2.484s
|user	0m1.564s | user	0m1.868s
|sys	0m0.228s | sys	0m0.524s
| at second run 
| real	0m1.245s | real	0m3.359s
| user	0m1.560s | user	0m2.016s
| sys	0m0.152s   | sys	0m1.168s

> note: this bench mark may differt accouding to system's working and to restult present here is exact same result in my system 
ububtu 4Gb RAM and i3 process. If I find another good benchmark techinque then I will change to it. 

Examples
=============

Chunk and NER use BIOS Tagging Scheme. Which expands to:

1. S = Tag covers Single Word.
2. B = Tag Begins with the Word.
3. I = Word is internal to tag which has begun.
4. E = Tag Ends with the Word.
5. 0 = Other tags.

Example:
<!---
  ('Biplab', 'S-NP'), ('is', 'S-VP'), ('a', 'B-NP'), ('good', 'I-NP'), ('boy', 'E-NP'), ('.', 'O')
---> 
('Republican', 'B-NP'), ('candidate', 'I-NP'), ('George', 'I-NP'), ('Bush', 'E-NP'), ('was', 'S-VP'), ('great', 'S-ADJP'), ('.', 'O')
  means:
  
[Republican]NP [candidate]NP [a good boy]NP [George]NP [Bush]NP [was]VP [great]ADJP
  

Annotator is the only class you need. Create an annotator object.

<pre>
pntl
| -- tools
     | --class-- Annotator
     | --jar-- stanford-parser
| -- utils
     | --function-- skipgrams

</pre>

>`in.parser` file consite syntax tree(for now) which is use as input for dependencie parser. One more thing the last runned sentence output only 
will be stored.

```python
>>>from pntl.tools import Annotator
>>>annotator = Annotator()
>>>#changing senna path at run time is also possible
>>>
>>>annotator.senna_dir = "/home/user/senna"
>>>annotator.senna_dir# return path name
"/home/user/senna"
>>>annotator.stp_dir = "/home/user/stanford_parser_folder"# stanfordparser.jar must present inside it.
>>>annotator.java_cli
java -cp stanford-parser.jar edu.stanford.nlp.trees.EnglishGrammaticalStructure -treeFile in.parse -collapsed
>>>
>>>annotator.java_cli = "java -cp stanford-parser.jar edu.stanford.nlp.trees.EnglishGrammaticalStructure -treeFile in.parse"
>>>#setting the cli
```
#### alter option for -treeFile [futur work]
Usage: java GrammaticalStructure [options]* [-sentFile|-treeFile|-conllxFile file] [-testGraph]
  options: -basic, -collapsed, -CCprocessed [the default], -collapsedTree, -parseTree, -test, -parserFile file, -conllx, -keepPunct, -altprinter -altreader -altreaderfile
> use -treeFile as default format and the `getDependency()` write tree format in `in.parser`, to use other option pls note write custome function is the best option taking `syntax_tree` as input format and by coverting into require format of users and please know what your doing to get favourable output or have to write custome module before passing to `getDependency()`(comming soon). 

Self-testing
============

To test for your self please use function `test()` 
### test(senna_path="",  sent="", dep_model="", batch=False)
senna_path: location of senna 

sent = tokenized string or list of string 

batch =  batch must be `True` if sent is a list of strings

```python
>>>from pntl.tools import test
>>>test(senna_path="/home/user/senna")# input the location of senna file, if the senna is present the follwing output is printed
dep_parse:
 nsubj(created-2, He-1)
root(ROOT-0, created-2)
det(robot-4, the-3)
dobj(created-2, robot-4)
conj_and(created-2, broke-6)
dobj(broke-6, it-7)
prepc_after(broke-6, making-9)
dobj(making-9, it.-10)
chunk:
 [('He', 'S-NP'), ('created', 'S-VP'), ('the', 'B-NP'), ('robot', 'E-NP'), ('and', 'O'), ('broke', 'S-VP'), ('it', 'S-NP'), ('after', 'S-PP'), ('making', 'S-VP'), ('it.', 'S-NP')]
pos:
 [('He', 'PRP'), ('created', 'VBD'), ('the', 'DT'), ('robot', 'NN'), ('and', 'CC'), ('broke', 'VBD'), ('it', 'PRP'), ('after', 'IN'), ('making', 'VBG'), ('it.', 'PRP')]
ner:
 [('He', 'O'), ('created', 'O'), ('the', 'O'), ('robot', 'O'), ('and', 'O'), ('broke', 'O'), ('it', 'O'), ('after', 'O'), ('making', 'O'), ('it.', 'O')]
srl:
 [{'A1': 'the robot', 'V': 'created', 'A0': 'He'}, {'A1': 'it', 'AM-TMP': 'after making it.', 'V': 'broke', 'A0': 'He'}, {'A1': 'it.', 'V': 'making', 'A0': 'He'}]
syntax tree:
 (S1(S(NP(PRP He))(VP(VP(VBD created)(NP(DT the)(NN robot)))(CC and)(VP(VBD broke)(NP(PRP it))(PP(IN after)(S(VP(VBG making)(NP(PRP it.)))))))))
words:
 ['He', 'created', 'the', 'robot', 'and', 'broke', 'it', 'after', 'making', 'it.']
skip gram
 [('He', 'created', 'the'), ('He', 'created', 'robot'), ('He', 'created', 'and'), ('He', 'the', 'robot'), ('He', 'the', 'and'), ('He', 'robot', 'and'), ('created', 'the', 'robot'), ('created', 'the', 'and'), ('created', 'the', 'broke'), ('created', 'robot', 'and'), ('created', 'robot', 'broke'), ('created', 'and', 'broke'), ('the', 'robot', 'and'), ('the', 'robot', 'broke'), ('the', 'robot', 'it'), ('the', 'and', 'broke'), ('the', 'and', 'it'), ('the', 'broke', 'it'), ('robot', 'and', 'broke'), ('robot', 'and', 'it'), ('robot', 'and', 'after'), ('robot', 'broke', 'it'), ('robot', 'broke', 'after'), ('robot', 'it', 'after'), ('and', 'broke', 'it'), ('and', 'broke', 'after'), ('and', 'broke', 'making'), ('and', 'it', 'after'), ('and', 'it', 'making'), ('and', 'after', 'making'), ('broke', 'it', 'after'), ('broke', 'it', 'making'), ('broke', 'it', 'it.'), ('broke', 'after', 'making'), ('broke', 'after', 'it.'), ('broke', 'making', 'it.'), ('it', 'after', 'making'), ('it', 'after', 'it.'), ('it', 'making', 'it.'), ('after', 'making', 'it.')]

```

>Run the `depParser.sh` for English PCFG parser on one or more files, printing trees only

Error:
(Unable to resolve "edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz" as either class path, filename or URL)
then you should have CoreNLP(Stanford).

> To know about examples and issues look at my [wiki page](https://github.com/jawahar273/practNLPTools-lite/wiki)

