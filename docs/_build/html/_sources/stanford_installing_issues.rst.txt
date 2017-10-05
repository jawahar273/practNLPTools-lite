If there is an issue in stanford parser.
----------------------------------------

If the stanford parser can not be copy into installing location. So for
quick working on Dependence parser the some possible.

#. Assigning the location of ``stanford-parser.jar``.

   .. code:: python

       annotator=Annotator()
       annotator.stp_dir="location_pls"#with respect to your os environment or follow the below steps

#. Placing the ``stanford-parser.jar`` explicitly inside the installing
   in linux on python 3.x usual location is
   ``/usr/local/lib/python3.5/dist-packages/pntl``
#. if you are using Anaconda distribution python the possible location
   is ``/home/<user_name>/anaconda3/lib/python3.5/site-packages/pntl/``
   (without ``virtual environment``)
#. | For Windows if you have install python in ``C:`` the go to the path
   | ``c:\users\<user_name_here>\local\programs\python3<just_version_number_here>\lib\site-packages\pntl``
   | or for Anaconda Python distribution
     ``C:\anaconda3\Lib\site-packages\pntl``

| Eg:
| ``c:\users\jawahar\local\programs\python35\lib\site-packages\pntl``
| this is an example path with Python 3.5 installed in Windows system
  with jawahar as its user name.

    Note:- In Anaconda distribution it has its own version number so
    please change if you have to and change the Python version according
    which is present in your system. For windows there is no need to
    ``.``\ (dot) in between version number of Python.

Don’t forget to make ``sudo python setup install`` or admin terminal ``python setup install``
=============================================================================================