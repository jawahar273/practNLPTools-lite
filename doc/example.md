# Welcome to the practNLPTools-lite wiki!

## Examples:

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


Using Function getAnnoations(sentence) returns a dictionary of annotations.
```python
 >>>annotator.getAnnotations("There are people dying make this world a better place for you and for me.")
    {'dep_parse': '', 'chunk': [('There', 'S-NP'), ('are', 'S-VP'), ('people', 'S-NP'), ('dying', 'B-VP'), ('make', 'E-VP'), ('this', 'B-NP'), ('world', 'E-NP'), ('a', 'B-NP'), ('better', 'I-NP'), ('place', 'E-NP'), ('for', 'S-PP'), ('you', 'S-NP'), ('and', 'O'), ('for', 'S-PP'), ('me.', 'S-NP')], 'pos': [('There', 'EX'), ('are', 'VBP'), ('people', 'NNS'), ('dying', 'VBG'), ('make', 'VB'), ('this', 'DT'), ('world', 'NN'), ('a', 'DT'), ('better', 'JJR'), ('place', 'NN'), ('for', 'IN'), ('you', 'PRP'), ('and', 'CC'), ('for', 'IN'), ('me.', '.')], 'srl': [{'A1': 'people', 'V': 'dying'}, {'A1': 'people  this world', 'A2': 'a better place for you and for me.', 'V': 'make'}], 'syntax_tree': '(S1(S(NP(EX There))(VP(VBP are)(NP(NP(NNS people))(SBAR(S(VBG dying)(VP(VB make)(S(NP(DT this)(NN world))(NP(DT a)(JJR better)(NN place)))(PP(PP(IN for)(NP(PRP you)))(CC and)(PP(IN for)(NP(. me.)))))))))))', 'verbs': ['dying', 'make'], 'words': ['There', 'are', 'people', 'dying', 'make', 'this', 'world', 'a', 'better', 'place', 'for', 'you', 'and', 'for', 'me.'], 'ner': [('There', 'O'), ('are', 'O'), ('people', 'O'), ('dying', 'O'), ('make', 'O'), ('this', 'O'), ('world', 'O'), ('a', 'O'), ('better', 'O'), ('place', 'O'), ('for', 'O'), ('you', 'O'), ('and', 'O'), ('for', 'O'), ('me.', 'O')]}
```

Using Function getAnnoations(sentence,dep_parse=True) returns a dictionary of annotations with dependency parse, by default it is switched off.
```python
>>>annotator.getAnnotations("There are people dying make this world a better place for you and for me.",dep_parse=True)
    {'dep_parse': 'expl(are-2, There-1)\nroot(ROOT-0, are-2)\nnsubj(are-2, people-3)\ndep(make-5, dying-4)\nrcmod(people-3, make-5)\ndet(world-7, this-6)\nnsubj(place-10, world-7)\ndet(place-10, a-8)\namod(place-10, better-9)\nxcomp(make-5, place-10)\nprep_for(make-5, you-12)\nconj_and(you-12, me.-15)', 'chunk': [('There', 'S-NP'), ('are', 'S-VP'), ('people', 'S-NP'), ('dying', 'B-VP'), ('make', 'E-VP'), ('this', 'B-NP'), ('world', 'E-NP'), ('a', 'B-NP'), ('better', 'I-NP'), ('place', 'E-NP'), ('for', 'S-PP'), ('you', 'S-NP'), ('and', 'O'), ('for', 'S-PP'), ('me.', 'S-NP')], 'pos': [('There', 'EX'), ('are', 'VBP'), ('people', 'NNS'), ('dying', 'VBG'), ('make', 'VB'), ('this', 'DT'), ('world', 'NN'), ('a', 'DT'), ('better', 'JJR'), ('place', 'NN'), ('for', 'IN'), ('you', 'PRP'), ('and', 'CC'), ('for', 'IN'), ('me.', '.')], 'srl': [{'A1': 'people', 'V': 'dying'}, {'A1': 'people  this world', 'A2': 'a better place for you and for me.', 'V': 'make'}], 'syntax_tree': '(S1(S(NP(EX There))(VP(VBP are)(NP(NP(NNS people))(SBAR(S(VBG dying)(VP(VB make)(S(NP(DT this)(NN world))(NP(DT a)(JJR better)(NN place)))(PP(PP(IN for)(NP(PRP you)))(CC and)(PP(IN for)(NP(. me.)))))))))))', 'verbs': ['dying', 'make'], 'words': ['There', 'are', 'people', 'dying', 'make', 'this', 'world', 'a', 'better', 'place', 'for', 'you', 'and', 'for', 'me.'], 'ner': [('There', 'O'), ('are', 'O'), ('people', 'O'), ('dying', 'O'), ('make', 'O'), ('this', 'O'), ('world', 'O'), ('a', 'O'), ('better', 'O'), ('place', 'O'), ('for', 'O'), ('you', 'O'), ('and', 'O'), ('for', 'O'), ('me.', 'O')]}
```
You can access individual componets as:
```python
>>>annotator.getAnnotations("Biplab is a good boy.")['pos']
  [('Biplab', 'NNP'), ('is', 'VBZ'), ('a', 'DT'), ('good', 'JJ'), ('boy', 'NN'), ('.', '.')]
>>>annotator.getAnnotations("Biplab is a good boy.")['ner']
  [('Biplab', 'S-PER'), ('is', 'O'), ('a', 'O'), ('good', 'O'), ('boy', 'O'), ('.', 'O')]
>>>annotator.getAnnotations("Biplab is a good boy.")['chunk']
  [('Biplab', 'S-NP'), ('is', 'S-VP'), ('a', 'B-NP'), ('good', 'I-NP'), ('boy', 'E-NP'), ('.', 'O')]
```

To list the verbs for which semantic roles are found.
```python
>>>annotator.getAnnotations("He created the robot and broke it after making it.")['verbs']
   ['created', 'broke', 'making']
```
'srl' Returns a list of dictionaries, identifyinging sematic roles for various verbs in sentence.
```python
>>>annotator.getAnnotations("He created the robot and broke it after making it.")['srl']
    [{'A1': 'the robot', 'A0': 'He', 'V': 'created'}, {'A1': 'it', 'A0': 'He', 'AM-TMP': 'after making it.', 'V': 'broke'}, {'A1': 'it.', 'A0': 'He', 'V': 'making'}]
```
'syntax_tree' Returns syntax tree in penn Tree Bank Format.
```python
>>>annotator.getAnnotations("He created the robot and broke it after making it.")['syntax_tree']
    '(S1(S(NP(PRP He))(VP(VP(VBD created)(NP(DT the)(NN robot)))(CC and)(VP(VBD broke)(NP(PRP it))(PP(IN after)(S(VP(VBG making)(NP(PRP it.)))))))))'
```
'dep_parse' Returns dependency Relations as a string. Each relation is in new line. You may require some post processing on this.

> Notes: dep_parse may not work properly if stanford dependency parser is not present in practnlptools folder.
To change in the output format from edit `lexparser.sh`(self testing only) if you know what you are doing

To know about `outputformat` see the Stanford Parser FAQ [link](https://nlp.stanford.edu/software/parser-faq.shtml#u) and manuall [link](https://nlp.stanford.edu/software/dependencies_manual.pdf).
```python
>>> annotator.getAnnotations("He created the robot and broke it after making it.",dep_parse=True)['dep_parse']
    nsubj(created-2, He-1)
    root(ROOT-0, created-2)
    det(robot-4, the-3)
    dobj(created-2, robot-4)
    conj_and(created-2, broke-6)
    dobj(broke-6, it-7)
    prepc_after(broke-6, making-9)
    dobj(making-9, it.-10)
```

If there are many sentences to annotate, Use batch Mode, annotator.getBatchAnnotations(sentences,dep_parse=True/False). Returns a list of annotation dictionaries.
```python
>>>annotator.getBatchAnnotations(["He created the robot and broke it after making it.","Biplab is a good boy."],dep_parse=True)
    [{'dep_parse': 'nsubj(created-2, He-1)\nroot(ROOT-0, created-2)\ndet(robot-4, the-3)\ndobj(created-2, robot-4)\nconj_and(created-2, broke-6)\ndobj(broke-6, it-7)\nprepc_after(broke-6, making-9)\ndobj(making-9, it.-10)', 'chunk': [('He', 'S-NP'), ('created', 'S-VP'), ('the', 'B-NP'), ('robot', 'E-NP'), ('and', 'O'), ('broke', 'S-VP'), ('it', 'S-NP'), ('after', 'S-PP'), ('making', 'S-VP'), ('it.', 'S-NP')], 'pos': [('He', 'PRP'), ('created', 'VBD'), ('the', 'DT'), ('robot', 'NN'), ('and', 'CC'), ('broke', 'VBD'), ('it', 'PRP'), ('after', 'IN'), ('making', 'VBG'), ('it.', 'PRP')], 'srl': [{'A1': 'the robot', 'A0': 'He', 'V': 'created'}, {'A1': 'it', 'A0': 'He', 'AM-TMP': 'after making it.', 'V': 'broke'}, {'A1': 'it.', 'A0': 'He', 'V': 'making'}], 'syntax_tree': '(S1(S(NP(PRP He))(VP(VP(VBD created)(NP(DT the)(NN robot)))(CC and)(VP(VBD broke)(NP(PRP it))(PP(IN after)(S(VP(VBG making)(NP(PRP it.)))))))))', 'verbs': ['created', 'broke', 'making'], 'words': ['He', 'created', 'the', 'robot', 'and', 'broke', 'it', 'after', 'making', 'it.'], 'ner': [('He', 'O'), ('created', 'O'), ('the', 'O'), ('robot', 'O'), ('and', 'O'), ('broke', 'O'), ('it', 'O'), ('after', 'O'), ('making', 'O'), ('it.', 'O')]}, {'dep_parse': 'nsubj(boy-5, Biplab-1)\ncop(boy-5, is-2)\ndet(boy-5, a-3)\namod(boy-5, good-4)\nroot(ROOT-0, boy-5)', 'chunk': [('Biplab', 'S-NP'), ('is', 'S-VP'), ('a', 'B-NP'), ('good', 'I-NP'), ('boy', 'E-NP'), ('.', 'O')], 'pos': [('Biplab', 'NNP'), ('is', 'VBZ'), ('a', 'DT'), ('good', 'JJ'), ('boy', 'NN'), ('.', '.')], 'srl': [], 'syntax_tree': '(S1(S(NP(NNP Biplab))(VP(VBZ is)(NP(DT a)(JJ good)(NN boy)))(. .)))', 'verbs': [], 'words': ['Biplab', 'is', 'a', 'good', 'boy', '.'], 'ner': [('Biplab', 'S-PER'), ('is', 'O'), ('a', 'O'), ('good', 'O'), ('boy', 'O'), ('.', 'O')]}]
```

Note: For illustration purposes we have used:
```python
>>>annotator.getAnnotations("He created the robot and broke it after making it.",dep_parse=True)['dep_parse']
```
Better method is:
```python
>>>annotation=annotator.getAnnotations("He created the robot and broke it after making it.",dep_parse=True)
>>>ner=annotation['ner']
>>>srl=annotation['srl']
```

```python
>>>from pntl.utils import skipgrams
>>>sent = "He created the robot and broke it after making it."
>>>#return generators
>>>list(skipgrams(sent.split(), n=3, k=2))
[('He', 'created', 'the'), ('He', 'created', 'robot'), ('He', 'created', 'and'), ('He', 'the', 'robot'), ('He', 'the', 'and'), ('He', 'robot', 'and'), ('created', 'the', 'robot'), ('created', 'the', 'and'), ('created', 'the', 'broke'), ('created', 'robot', 'and'), ('created', 'robot', 'broke'), ('created', 'and', 'broke'), ('the', 'robot', 'and'), ('the', 'robot', 'broke'), ('the', 'robot', 'it'), ('the', 'and', 'broke'), ('the', 'and', 'it'), ('the', 'broke', 'it'), ('robot', 'and', 'broke'), ('robot', 'and', 'it'), ('robot', 'and', 'after'), ('robot', 'broke', 'it'), ('robot', 'broke', 'after'), ('robot', 'it', 'after'), ('and', 'broke', 'it'), ('and', 'broke', 'after'), ('and', 'broke', 'making'), ('and', 'it', 'after'), ('and', 'it', 'making'), ('and', 'after', 'making'), ('broke', 'it', 'after'), ('broke', 'it', 'making'), ('broke', 'it', 'it.'), ('broke', 'after', 'making'), ('broke', 'after', 'it.'), ('broke', 'making', 'it.'), ('it', 'after', 'making'), ('it', 'after', 'it.'), ('it', 'making', 'it.'), ('after', 'making', 'it.')]
```
###### pnlt.utils.skipgrams(sentence, n=2, k=1)
n = is the value for n-grams
k = skip value 
 `skipgrams()` returns the output in genetator form for better memory management.



