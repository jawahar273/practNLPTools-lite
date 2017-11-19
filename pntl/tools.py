
# encoding: utf-8
# Practical Natural Language Processing Tools (practNLPTools-lite):
#               Combination of Senna and Stanford dependency Extractor
# Copyright (C) 2017 PractNLP-lite Project
# Current Author: Jawahar S <jawahar273@gmail.com>
# URL: https://jawahar273.gitbooks.io (or) https://github.com/jawahar273


from __future__ import generators, print_function, unicode_literals
import subprocess

import os
from platform import architecture, system

try:
    from colorama import init
    from colorama.Fore import RED, BLUE
    init(autoreset=True)
except ImportError:
    RED = " "
    BLUE = " "


class Annotator:
    """
    :param str senna_dir: path where is located
    :param str dep_model: Stanford dependencie mode
    :param str stp_dir: path of stanford parser jar
    :param str raise_e: raise exception if stanford-parser.jar
                        is not found
    """

    def __init__(self, senna_dir='', stp_dir='',
                 dep_model='edu.stanford.nlp.trees.'
                           'EnglishGrammaticalStructure',
                 raise_e=False):
        """
        init function of Annotator class
        """
        self.senna_path = ''
        self.dep_par_path = ''

        if not senna_dir:
            if 'SENNA' in os.environ:
                self.senna_path = os.path.normpath(os.environ['SENNA'])
                self.senna_path + os.path.sep
                exe_file_2 = self.get_senna_bin(self.senna_path)
                if not os.path.isfile(exe_file_2):
                    raise OSError(RED +
                                  "Senna executable expected at %s or"
                                  " %s but not found"
                                  % (self.senna_path, exe_file_2))
        elif senna_dir.startswith('.'):
            self.senna_path = os.path.realpath(senna_dir) + os.path.sep
        else:
            self.senna_path = senna_dir.strip()
            self.senna_path = self.senna_path.rstrip(os.path.sep) + os.path.sep

        if not stp_dir:
            import pntl.tools as Tfile
            self.dep_par_path = Tfile.__file__.rsplit(os.path.sep, 1)[0] + os.path.sep
            self.check_stp_jar(self.dep_par_path, raise_e=True)
        else:
            self.dep_par_path = stp_dir + os.path.sep
            self.check_stp_jar(self.dep_par_path, raise_e)

        self.dep_par_model = dep_model
        # print(dep_model)

        self.default_jar_cli = ['java', '-cp', 'stanford-parser.jar',
                                self.dep_par_model,
                                '-treeFile', 'in.parse', '-collapsed']
        self.print_values()

    def print_values(self):
        """ displays the current set of values
        such as SENNA location, stanford parser jar,
        jar command interface
        """
        print("**" * 50)
        print("default values:\nsenna path:\n", self.senna_path,
              "\nDependencie parser:\n", self.dep_par_path)
        # print(self.default_jar_cli)
        print("Stanford parser clr", " ".join(self.default_jar_cli))
        print("**" * 50)

    def check_stp_jar(self, path, raise_e=False, _rec=True):
        """Check the stanford parser is present in the given directions
        and nested searching will be added in futurwork

        :param str path: path of where the stanford parser is present
        :param bool raise_e: to raise exception with user
              wise and default `False` don't raises exception
        :return: given path if it is valid one or return boolean `False` or
             if raise FileNotFoundError on raise_exp=True
        :rtype: bool

        """
        gpath = path
        path = os.listdir(path)
        file_found = False
        for file in path:
            if file.endswith(".jar"):
                if file.startswith("stanford-parser"):
                    file_found = True
        if not file_found:
            # need to check the install dir for stanfor parser
            if _rec:
                import pntl
                path_ = os.path.split(pntl.__file__)[0]
                self.check_stp_jar(path_, raise_e, _rec=False)
            if raise_e:
                raise FileNotFoundError(RED + "`stanford-parser.jar` is "
                                        "not"
                                        " found in the path \n"
                                        "`{}` \n"
                                        "To know about more about the issues,"
                                        "got to this given link ["
                                        "http://pntl.readthedocs.io/en/"
                                        "latest/stanford_installing_"
                                        "issues.html] \n User "
                                        "`pntl -I true` to downlard "
                                        "needed file automatically."
                                        .format(gpath))
        return file_found

    @property
    def stp_dir(self):
        """The return the path of stanford parser jar location
        and set the path for Dependency Parse at run time(
        this is python @property)
        """
        return self.dep_par_path

    @stp_dir.setter
    def stp_dir(self, val):
        if os.path.isdir(val):
            self.dep_par_path = val + os.path.sep

    @property
    def senna_dir(self):
        """The return the path of senna location
        and set the path for senna at run time(this is python @property)

        :rtype: string
        """
        return self.senna_path

    @senna_dir.setter
    def senna_dir(self, val):
        if os.path.isdir(val):
            self.senna_path = val + os.path.sep

    @property
    def jar_cli(self):
        """
        The return cli for standford-parser.jar(this is python @property)

        :rtype: string
        """
        return " ".join(self.default_jar_cli)

    @jar_cli.setter
    def jar_cli(self, val):
        self.default_jar_cli = val.split()

    def get_senna_bin(self, os_name):
        """
        get the current os executable binary file.

        :param str os_name: os name like Linux, Darwin, Windows
        :return: the corresponding exceutable object file of senna
        :rtype: str
        """

        if os_name == 'Linux':
            bits = architecture()[0]
            if bits == '64bit':
                executable = 'senna-linux64'
            elif bits == '32bit':
                executable = 'senna-linux32'
            else:
                executable = 'senna'
        elif os_name == 'Darwin':
            executable = 'senna-osx'
        elif os_name == 'Windows':
            executable = 'senna-win32.exe'
        return self.senna_path + executable

    def get_senna_tag_batch(self, sentences):
        """
        Communicates with senna through lower level communiction(sub process)
        and converted the console output(default is file writing).
        On batch processing each end is add with new line.

        :param list sentences: list of sentences for batch processes
        :rtype: str
        """
        input_data = ""
        for sentence in sentences:
            input_data += sentence + "\n"
        input_data = input_data[:-1]
        package_directory = os.path.dirname(self.senna_path)
        os_name = system()
        executable = self.get_senna_bin(os_name)
        senna_executable = os.path.join(package_directory, executable)
        cwd = os.getcwd()
        os.chdir(package_directory)
        pipe = subprocess.Popen(senna_executable,
                                stdout=subprocess.PIPE,
                                stdin=subprocess.PIPE,
                                shell=True)
        senna_stdout = pipe.communicate(input=input_data.encode('utf-8'))[0]
        os.chdir(cwd)
        return senna_stdout.decode().split("\n\n")[0:-1]

    @classmethod
    def help_conll_format(cls):
        """With the help of this method, detail of senna
         arguments are displayed
        """
        return cls.get_conll_format.__doc__.split("\n\n")[1]

    def get_conll_format(self, sentence, options='-srl -pos -ner -chk -psg'):
        """Communicates with senna through lower level communiction
        (sub process) and converted the console output(default is file writing)
        with CoNLL format and argument to be in `options` pass

        :param str or list: list of sentences for batch processes
        :param  options list: list of arguments
+--------------+-----------------------------------------------+
| options      | desc                                          |
+==============+===============================================+
| -verbose     | Display model informations (on the standard   |
|              | error output, so it does not mess up the tag  |
|              | outputs).                                     |
+--------------+-----------------------------------------------+
| -notokentags | Do not output tokens (first output column).   |
+--------------+-----------------------------------------------+
| -offsettags  | Output start/end character offset (in the     |
|              | sentence), for each token.                    |
+--------------+-----------------------------------------------+
| -iobtags     | Output IOB tags instead of IOBES.             |
+--------------+-----------------------------------------------+
| -brackettags | Output ‘bracket’ tags instead of IOBES.       |
+--------------+-----------------------------------------------+
| -path        | Specify the path to the SENNA data and hash   |
|              | directories, if you do not run SENNA in its   |
|              | original directory. The path must end by “/”. |
+--------------+-----------------------------------------------+
| -usrtokens   | Use user’s tokens (space separated) instead   |
|              | of SENNA tokenizer.                           |
+--------------+-----------------------------------------------+
| -posvbs      | Use verbs outputed by the POS tagger instead  |
|              | of SRL style verbs for SRL task. You might    |
|              | want to use this, as the SRL training task    |
|              | ignore some verbs (many “be” and “have”)      |
|              | which might be not what you want.             |
+--------------+-----------------------------------------------+
| -usrvbs      | Use user’s verbs (given in ) instead of SENNA |
|              | verbs for SRL task. The file must contain one |
|              | line per token, with an empty line between    |
|              | each sentence. A line which is not a “-”      |
|              | corresponds to a verb.                        |
+--------------+-----------------------------------------------+
| -pos         | Instead of outputing tags for all tasks,      |
|              | SENNA will output tags for the specified (one |
|              | or more) tasks.                               |
+--------------+-----------------------------------------------+
| -chk         | Instead of outputing tags for all tasks,      |
|              | SENNA will output tags for the specified (one |
|              | or more) tasks.                               |
+--------------+-----------------------------------------------+
| -ner         | Instead of outputing tags for all tasks,      |
|              | SENNA will output tags for the specified (one |
|              | or more) tasks.                               |
+--------------+-----------------------------------------------+
| -srl         | Instead of outputing tags for all tasks,      |
|              | SENNA will output tags for the specified (one |
|              | or more) tasks.                               |
+--------------+-----------------------------------------------+
| -psg         | Instead of outputing tags for all tasks,      |
|              | SENNA will output tags for the specified (one |
|              | or more) tasks.                               |
+--------------+-----------------------------------------------+

        :return: senna tagged output
        :rtype: str
        """
        if isinstance(options, str):
            options = options.strip().split()

        input_data = sentence
        package_directory = os.path.dirname(self.senna_path)
        os_name = system()
        executable = self.get_senna_bin(os_name)
        senna_executable = os.path.join(executable)
        # print("testing dir", executable, package_directory)
        cwd = os.getcwd()
        os.chdir(package_directory)
        args = [senna_executable]
        args.extend(options)
        pipe = subprocess.Popen(args,
                                stdout=subprocess.PIPE,
                                stdin=subprocess.PIPE,
                                shell=True)
        senna_stdout = pipe.communicate(input=" ".join(input_data)
                                        .encode('utf-8'))[0]
        os.chdir(cwd)
        return senna_stdout.decode("utf-8").strip()

    def get_senna_tag(self, sentence):
        """
        Communicates with senna through lower level communiction(sub process)
        and converted the console output(default is file writing)

        :param str/list listsentences : list of sentences for batch processes
        :return: senna tagged output
        :rtype: str
        """
        input_data = sentence
        package_directory = os.path.dirname(self.senna_path)
        # print("testing dir",self.dep_par_path, package_directory)
        os_name = system()
        executable = self.get_senna_bin(os_name)
        senna_executable = os.path.join(package_directory, executable)
        cwd = os.getcwd()
        os.chdir(package_directory)
        pipe = subprocess.Popen(senna_executable,
                                stdout=subprocess.PIPE,
                                stdin=subprocess.PIPE,
                                shell=True)
        senna_stdout = pipe.communicate(input=" ".join(input_data)
                                        .encode('utf-8'))[0]
        os.chdir(cwd)
        return senna_stdout

    def get_dependency(self, parse):
        """
        Change to the Stanford parser direction and process the works

        :param str parse: parse is the input(tree format)
                  and it is writen in as file

        :return: stanford dependency universal format
        :rtype: str
        """
        # print("\nrunning.........")
        package_directory = os.path.dirname(self.dep_par_path)
        cwd = os.getcwd()
        os.chdir(package_directory)

        with open(self.senna_path + os.path.sep + "in.parse",
                  "w", encoding='utf-8') as parsefile:
            parsefile.write(parse)
        pipe = subprocess.Popen(self.default_jar_cli,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                shell=True)
        pipe.wait()

        stanford_out = pipe.stdout.read()
        # print(stanford_out, "\n", self.default_jar_cli)
        os.chdir(cwd)

        return stanford_out.decode("utf-8").strip()

    def get_batch_annotations(self, sentences, dep_parse=True):
        """
        :param list sentences: list of sentences
        :rtype: dict
        """
        annotations = []
        batch_senna_tags = self.get_senna_tag_batch(sentences)
        for senna_tags in batch_senna_tags:
            annotations += [self.get_annoations(senna_tags=senna_tags)]
        if dep_parse:
            syntax_tree = ""
            for annotation in annotations:
                syntax_tree += annotation['syntax_tree']
            dependencies = self.get_dependency(syntax_tree).split("\n\n")
            # print (dependencies)
            if len(annotations) == len(dependencies):
                for dependencie, annotation in zip(dependencies, annotations):
                    annotation["dep_parse"] = dependencie
        return annotations

    def get_annoations(self, sentence='', senna_tags=None, dep_parse=True):
        """
        passing the string to senna and performing aboue given nlp process
        and the returning them in a form of `dict()`

        :param str or list sentence: a sentence or list of
                     sentence for nlp process.
        :param str or list senna_tags:  this values are by
                     SENNA processed string
        :param bool  batch: the change the mode into batch
                     processing process
        :param bool dep_parse: to tell the code and user need
                    to communicate with stanford parser
        :return: the dict() of every out in the process
                    such as ner, dep_parse, srl, verbs etc.
        :rtype: dict
        """
        annotations = {}
        if not senna_tags:
            senna_tags = self.get_senna_tag(sentence).decode()
            senna_tags = [x.strip() for x in senna_tags.split("\n")]
            senna_tags = senna_tags[0:-2]
        else:
            senna_tags = [x.strip() for x in senna_tags.split("\n")]
        no_verbs = len(senna_tags[0].split("\t")) - 6

        words = []
        pos = []
        chunk = []
        ner = []
        verb = []
        srls = []
        syn = []
        for senna_tag in senna_tags:
            senna_tag = senna_tag.split("\t")
            words += [senna_tag[0].strip()]
            pos += [senna_tag[1].strip()]
            chunk += [senna_tag[2].strip()]
            ner += [senna_tag[3].strip()]
            verb += [senna_tag[4].strip()]
            srl = []
            for i in range(5, 5 + no_verbs):
                srl += [senna_tag[i].strip()]
            srls += [tuple(srl)]
            syn += [senna_tag[-1]]
        roles = []
        for j in range(no_verbs):
            role = {}
            i = 0
            temp = ""
            curr_labels = [x[j] for x in srls]
            for curr_label in curr_labels:
                splits = curr_label.split("-")
                if splits[0] == "S":
                    if len(splits) == 2:
                        if splits[1] == "V":
                            role[splits[1]] = words[i]
                        else:
                            if splits[1] in role:
                                role[splits[1]] += " " + words[i]
                            else:
                                role[splits[1]] = words[i]
                    elif len(splits) == 3:
                        if splits[1] + "-" + splits[2] in role:
                            role[splits[1] + "-" + splits[2]] += " " + words[i]
                        else:
                            role[splits[1] + "-" + splits[2]] = words[i]
                elif splits[0] == "B":
                    temp = temp + " " + words[i]
                elif splits[0] == "I":
                    temp = temp + " " + words[i]
                elif splits[0] == "E":
                    temp = temp + " " + words[i]
                    if len(splits) == 2:
                        if splits[1] == "V":
                            role[splits[1]] = temp.strip()
                        else:
                            if splits[1] in role:
                                role[splits[1]] += " " + temp
                                role[splits[1]] = role[splits[1]].strip()
                            else:
                                role[splits[1]] = temp.strip()
                    elif len(splits) == 3:
                        if splits[1] + "-" + splits[2] in role:
                            role[splits[1] + "-" + splits[2]] += " " + temp
                            role[splits[1] + "-" + splits[2]] = role[splits[1] + "-" + splits[2]].strip()
                        else:
                            role[splits[1] + "-" + splits[2]] = temp.strip()
                    temp = ""
                i += 1
            if "V" in role:
                roles += [role]
        annotations['words'] = words
        annotations['pos'] = list(zip(words, pos))
        annotations['ner'] = list(zip(words, ner))
        annotations['srl'] = roles
        annotations['verbs'] = [x for x in verb if x != "-"]
        annotations['chunk'] = list(zip(words, chunk))
        annotations['dep_parse'] = ""
        annotations['syntax_tree'] = ""
        for (word_, syn_, pos_) in zip(words, syn, pos):
            annotations['syntax_tree'] += syn_.replace("*", "(" + pos_ + " " + word_ + ")")
        #annotations['syntax_tree']=annotations['syntax_tree'].replace("S1","S")
        if dep_parse:
            annotations['dep_parse'] = self.get_dependency(annotations
                                                           ['syntax_tree'])
        return annotations


def test(senna_path='', sent='',
         dep_model='',
         batch=False,
         stp_dir=''):
    """please replace the path of yours environment(according to OS path)

    .. warning::
       deprecated:: 0.2.0.
       See CLI doc instead. This `test()` function will be removed from next release.

    :param str senna_path: path for senna location \n
    :param str dep_model: stanford dependency parser model location \n
    :param str or list sent: the sentence to process with Senna \n
    :param bool batch:  processing more than one sentence
       in one row \n
    :param str stp_dir: location of stanford-parser.jar file

    """
    from pntl.utils import skipgrams
    annotator = Annotator(senna_path, stp_dir, dep_model)
    if not sent and batch:
        sent = ["He killed the man with a knife and murdered"
                "him with a dagger.",
                "He is a good boy.",
                "He created the robot and broke it after making it."]
    elif not sent:
        sent = 'get me a hotel on chennai in 21-4-2017 '
        # "He created the robot and broke it after making it.
    if not batch:
        print("\n", sent, "\n")
        sent = sent.split()
        args = '-srl -pos'.strip().split()
        print("conll:\n", annotator.get_conll_format(sent, args))
        temp = annotator.get_annoations(sent, dep_parse=True)['dep_parse']
        print('dep_parse:\n', temp)
        temp = annotator.get_annoations(sent, dep_parse=True)['chunk']
        print('chunk:\n', temp)
        temp = annotator.get_annoations(sent, dep_parse=True)['pos']
        print('pos:\n', temp)
        temp = annotator.get_annoations(sent, dep_parse=True)['ner']
        print('ner:\n', temp)
        temp = annotator.get_annoations(sent, dep_parse=True)['srl']
        print('srl:\n', temp)
        temp = annotator.get_annoations(sent,
                                        dep_parse=True)['syntax_tree']
        print('syntaxTree:\n', temp)
        temp = annotator.get_annoations(sent, dep_parse=True)['words']
        print('words:\n', temp)
        print('skip gram\n', list(skipgrams(sent, n=3, k=2)))

    else:
        print("\n\nrunning batch process", "\n", "=" * 20,
              "\n", sent, "\n")
        args = '-srl -pos'.strip().split()
        print("conll:\n", annotator.get_conll_format(sent, args))
        print(BLUE + "CoNLL format is recommented for batch process")
