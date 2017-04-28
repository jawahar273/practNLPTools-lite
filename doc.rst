
        .. py:property::senna_dir

        The return the path of senna location
        and set the path for senna at run time
        :rtype: string
        
        init function of Annotator class
        str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.
         .. py:method:: getDependency(parse)

         change to the Stanford parser direction and process the works

         :param parse: parse is the input(tree format) and it is writen in as file
         :type parse: string
         :return: stanford dependency universal format
         :rtype: string
        
        .. py:method:: getSennaTagBatch(sentences)

        Communicates with senna through lower level communiction(sub process)
        and converted the console output(default is file writing).
        On batch processing each end is add with new line.

        :param sentences: list of sentences for batch processes
        :type sentences:list of strings
        :rtype: string
        dictionary for instance variables (if defined)list of weak references to the object (if defined)
          .. py:function:: check_stp_jar(path, raise_exp=False, nested=False)

          :param path: path of where the stanford parser is present
          :param raise_exp: to raise exception with user wise and default `False`
              don't raises exception
          :param nested: walk through each sub-direction on the given location
          :type path: string
          :type raise_exp: boolean
          :type nested: boolean
          :return: given path if it is valid one or return boolean `False` or
             if raise Exception on raise_exp=True
          :rtype: bool or string
        Work in progess...........................
        
        .. py:property::stp_dir

        The return the path of senna location
        and set the path for senna at run time
        
        .. py:method:: getAnnotations(sentence="", senna_tags=None, batch=False, dep_parse=True)

        passing the string to senna and performing aboue given nlp process
        and the returning them in a form of `dict()`

        :parama sentence: a sentence or list of sentence for nlp process.
        :parama senna_tags: this on use value and this values are by SENNA processed string
        :parama batch: the change the mode into batch processing process
        :param dep_parse: to tell the code and user need to communicate with stanford parser
        :type sentence: string or list
        :type senna_tags: string or list
        :type batch: bool
        :type dep_parse: bool
        :return: the dict() of every out in the process such as ner, dep_parse, srl, verbs etc.
        :rtype: dict
        
        .. py:method:: print_values

        displays the current set of values such as SENNA location, stanford parser jar,
          jar command interface
        "
        .. py:method:: get_cos_name

        get the executable binary with respect to the Os name.

        :param os_name: os name like Linux, Darwin, Windows
        :type os_name: string
        :return: the corresponding exceutable object file of senna 
        :rtype: string
        str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.
          .. Deprecation function:: getBatchAnnotations

          :param sentences: list of sentences
          :type sentences: list
          :rtype: dict
        
        .. py:property::jar_cli

        The return cli for standford-parser.jar
        :rtype: string
        
        .. py:method:: getSennaTag(sentence)

        Communicates with senna through lower level communiction(sub process)
        and converted the console output(default is file writing)

        :param sentences: list of sentences for batch processes
        :type sentences:strings
        :return: senna tagged output
        :rtype: string
        
        .. py:property::senna_dir

        The return the path of senna location
        and set the path for senna at run time
        :rtype: string
        
        init function of Annotator class
        str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.
         .. py:method:: getDependency(parse)

         change to the Stanford parser direction and process the works

         :param parse: parse is the input(tree format) and it is writen in as file
         :type parse: string
         :return: stanford dependency universal format
         :rtype: string
        
        .. py:method:: getSennaTagBatch(sentences)

        Communicates with senna through lower level communiction(sub process)
        and converted the console output(default is file writing).
        On batch processing each end is add with new line.

        :param sentences: list of sentences for batch processes
        :type sentences:list of strings
        :rtype: string
        dictionary for instance variables (if defined)list of weak references to the object (if defined)
          .. py:function:: check_stp_jar(path, raise_exp=False, nested=False)

          :param path: path of where the stanford parser is present
          :param raise_exp: to raise exception with user wise and default `False`
              don't raises exception
          :param nested: walk through each sub-direction on the given location
          :type path: string
          :type raise_exp: boolean
          :type nested: boolean
          :return: given path if it is valid one or return boolean `False` or
             if raise Exception on raise_exp=True
          :rtype: bool or string
        Work in progess...........................
        
        .. py:property::stp_dir

        The return the path of senna location
        and set the path for senna at run time
        
        .. py:method:: getAnnotations(sentence="", senna_tags=None, batch=False, dep_parse=True)

        passing the string to senna and performing aboue given nlp process
        and the returning them in a form of `dict()`

        :parama sentence: a sentence or list of sentence for nlp process.
        :parama senna_tags: this on use value and this values are by SENNA processed string
        :parama batch: the change the mode into batch processing process
        :param dep_parse: to tell the code and user need to communicate with stanford parser
        :type sentence: string or list
        :type senna_tags: string or list
        :type batch: bool
        :type dep_parse: bool
        :return: the dict() of every out in the process such as ner, dep_parse, srl, verbs etc.
        :rtype: dict
        
        .. py:method:: print_values

        displays the current set of values such as SENNA location, stanford parser jar,
          jar command interface
        "
        .. py:method:: get_cos_name

        get the executable binary with respect to the Os name.

        :param os_name: os name like Linux, Darwin, Windows
        :type os_name: string
        :return: the corresponding exceutable object file of senna 
        :rtype: string
        str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.
          .. Deprecation function:: getBatchAnnotations

          :param sentences: list of sentences
          :type sentences: list
          :rtype: dict
        
        .. py:property::jar_cli

        The return cli for standford-parser.jar
        :rtype: string
        
        .. py:method:: getSennaTag(sentence)

        Communicates with senna through lower level communiction(sub process)
        and converted the console output(default is file writing)

        :param sentences: list of sentences for batch processes
        :type sentences:strings
        :return: senna tagged output
        :rtype: string
        