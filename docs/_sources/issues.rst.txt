Issues
------

#. You cannot give sentence with ‘(’ ‘)’, that is left bracket aor right
   bracket. It will end up in returning no result. So please clean
   Sentences before sending to annotator.
#. Other issue might be senna executable built for various platforms. I
   have not experienced it, but its highly probable. If you get this
   issuse:

Go to folder senna location

.. code:: c

        cd senna
        gcc -O3 -o senna-linux64 *.c  (For linux 64 bit)
        gcc -O3 -o senna-linux32 *.c  (For linux 32 bit)
        gcc -O3 -o senna-senna-osx *.c (For Mac)
        *windows: I never compiled C files in Windows.*
        python setup.py install

#. Any other, you can mail to Jawahar273@gmail.com
#. Issues with “pip install pntl” 

You might receive following Error while running:

.. code:: python

     Traceback (most recent call last):
     File "test.py", line 3, in <module>
        print a.getAnnotations("This is a test.")
      File "/usr/local/lib/python3.5/dist-packages/pntl/tools.py", line 206, in getAnnotations
        senna_tags=self.getSennaTag(sentence)
      File "/usr/local/lib/python3.5/dist-packages/pntl/tools.py", line 88, in getSennaTag
        p = subprocess.Popen(senna_executable,stdout=subprocess.PIPE, stdin=subprocess.PIPE)
      File "/usr/lib/python3.5/subprocess.py", line 679, in __init__
        errread, errwrite)
      File "/usr/lib/python3.5/subprocess.py", line 1249, in _execute_child
        raise child_exception
    OSError: [Errno 13] Permission denied

| To Fix this,you can do:
| ``shell  chmod -R +x /usr/local/lib/python3.5/dist-packages/pntl/``