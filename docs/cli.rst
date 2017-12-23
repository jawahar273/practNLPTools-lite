====
CLI
====

To run know more about the CLI entry point use ```pntl --help``` for detail help 
command

.. code:: bash

    pntl --help
    Usage: pntl [OPTIONS]

      please replace the path of yours environment(according to OS path)

      :param str senna_path: path for senna location

      :param str dep_model: stanford dependency parser model location

      :param str or list sent: the sentence to process with Senna

      :param bool batch:  processing more than one sentence    in one row

      :param str stp_dir: location of stanford-parser.jar file

    Options:
      -SE, --senna_path PATH  Set the direction of senna.
      -S, --sent TEXT         Testing sentence to passed in senna.
      -DM, --dep_model TEXT   Stanford dependency parser model location.
      -B, --batch BOOLEAN     Batch process.
      -SD, --stp_dir TEXT     Location of stanford-parser.jar file.
      -I, --init BOOLEAN      downlard files from github.
      --help                  Show this message and exit.



