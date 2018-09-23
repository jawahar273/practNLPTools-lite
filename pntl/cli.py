# -*- coding: utf-8 -*-

"""Console script for practnlptools_lite."""
import os.path
import click
import urllib.request

from pntl.tools import Annotator
from pntl.utils import skipgrams

from colorama import Fore, init

init(autoreset=True)


def download_files():

    stanford_parser_url = (
        "https://github.com/jawahar273"
        "/practNLPTools-lite/blob/master/pntl/"
        "stanford-parser.jar"
    )
    dep_parse_url = (
        "https://github.com/jawahar273/practNLPTools-lite"
        "/blob/master/pntl/depParse.sh"
    )
    lexparser_url = (
        "https://github.com/jawahar273/practNLPTools-lite"
        "/blob/master/pntl/lexparser.sh"
    )

    import pntl

    file_loc = os.path.split(pntl.__file__)[0]
    print(
        ("location {} and \n list of files \n \t{}" "\n \t{}" "\n \t{}").format(
            file_loc, "stanford-parser", "dependency sh", "lexparser sh"
        )
    )
    print(Fore.GREEN + "downloading depend on the Network speed \n\n")

    with urllib.request.urlopen(stanford_parser_url) as spl:

        with open(file_loc + os.path.sep + "stanford-parser.jar", "wb") as file:

            file.write(spl.read())

    print(Fore.GREEN + "downloading stanford-parser done..")

    with urllib.request.urlopen(lexparser_url) as lpl:

        with open(file_loc + os.path.sep + "depParse.sh", "wb") as file:

            file.write(lpl.read())

    print(Fore.GREEN + "downloading lexparser parse sh done..")

    with urllib.request.urlopen(dep_parse_url) as dpl:

        with open(file_loc + os.path.sep + "lexparser.sh", "wb") as file:

            file.write(dpl.read())

    print(Fore.GREEN + "downloading dependency parse sh done..")


def main(senna_path="", sent="", dep_model="", batch=False, stp_dir="", init=False):

    annotator = Annotator(senna_path, stp_dir, dep_model)

    if not sent and batch:

        sent = [
            "He killed the man with a knife and murdered" "him with a dagger.",
            "He is a good boy.",
            "He created the robot and broke it after making it.",
        ]

    elif not sent:

        sent = "He created the robot and broke it after making it."

    if not batch:

        print("\n", sent, "\n")

        sent = sent.split()
        args = "-srl -pos".strip().split()

        print("conll:\n", annotator.get_conll_format(sent, args))

        temp = annotator.get_annoations(sent, dep_parse=True)

        print("dep_parse:\n", temp["dep_parse"])

        print("chunk:\n", temp["chunk"])

        print("pos:\n", temp["pos"])

        print("ner:\n", temp["ner"])

        print("srl:\n", temp["srl"])

        print("syntaxTree:\n", temp["syntax_tree"])

        print("words:\n", temp["words"])

        print("skip gram\n", list(skipgrams(sent, n=3, k=2)))

    else:

        print("\n\nrunning batch process", "\n", "=" * 20, "\n", sent, "\n")

        args = "-srl -pos".strip().split()

        print("conll:\n", annotator.get_conll_format(sent, args))

        print(Fore.BLUE + "CoNLL format is recommented for batch process")

        print("pos:\n", annotator.get_annoations(sent)["pos"])


@click.command()
@click.option(
    "-SE", "--senna_path", help="Set the direction of senna.", default=os.path.sep
)
@click.option(
    "-S", "--sent", help="Testing sentence to passed in senna.", type=str, default=""
)
@click.option(
    "-DM",
    "--dep_model",
    help="Stanford dependency parser model location.",
    type=str,
    default="edu.stanford.nlp.trees.EnglishGrammaticalStructure",
)
@click.option("-B", "--batch", type=click.BOOL, help="Batch process.")
@click.option(
    "-SD", "--stp_dir", help="Location of stanford-parser.jar file.", type=str
)
@click.option(
    "-I", "--init", help="downlard files from github.", type=click.BOOL, default=False
)
@click.option(
    "-E", "--env", help="enable the environment", type=click.BOOL, default=False
)
@click.option("-P", "--env_path", help="environment file location")
def user_test(
    senna_path="",
    sent="",
    dep_model="",
    batch=False,
    stp_dir="",
    init=False,
    env=False,
    env_path="",
):
    """please replace the path/dirs of yours (according to Operating system's fromat)

    :param str senna_path: path for senna location \n
    :param str dep_model: stanford dependency parser model \t
     default='edu.stanford.nlp.trees.EnglishGrammaticalStructure'
    \n
    :param str or list sent: the sentence to process with Senna \n
    :param bool batch:  processing more than one sentence
       in one row \n
    :param str stp_dir: location of stanford-parser.jar file
    :param bool init: downlard files from github.
    :param bool env: status for reading environment file.
    :param str env_path: location of the environment file.

    .. note::
    The default file for environment variable is consider
    as `.env`. If you have `.env` in diffrent path then is
    it is good way to pass the location alone with file name.

    .. bash::
        # for linux
        # /home/user_name/.env

        # for windows
        # C://user_name//.env

        # this is a example for idea purpose.

    """
    if init:

        download_files()

    else:

        if env:

            from dotenv import load_dotenv

            if not env_path:

                from os import getcwd
                from pathlib import Path

                env_path = Path(getcwd()) / ".env"

            load_dotenv(dotenv_path=env_path)

        main(senna_path, sent, dep_model, batch, stp_dir)
