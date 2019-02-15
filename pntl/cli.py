# -*- coding: utf-8 -*-

"""Console script for practnlptools_lite."""
import os.path
import subprocess
import urllib.request

from colorama import Fore, init
import click

from pntl.tools import Annotator
from pntl.utils import skipgrams

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
    click.echo(
        ("location {} and \n list of files \n \t{}" "\n \t{}" "\n \t{}").format(
            file_loc, "stanford-parser", "dependency sh", "lexparser sh"
        )
    )
    click.echo(Fore.GREEN + "downloading depend on the Network speed \n\n")

    with urllib.request.urlopen(stanford_parser_url) as spl:

        with open(file_loc + os.path.sep + "stanford-parser.jar", "wb") as file:

            file.write(spl.read())

    click.echo(Fore.GREEN + "downloading stanford-parser done..")

    with urllib.request.urlopen(lexparser_url) as lpl:

        with open(file_loc + os.path.sep + "depParse.sh", "wb") as file:

            file.write(lpl.read())

    click.echo(Fore.GREEN + "downloading lexparser parse sh done..")

    with urllib.request.urlopen(dep_parse_url) as dpl:

        with open(file_loc + os.path.sep + "lexparser.sh", "wb") as file:

            file.write(dpl.read())

    click.echo(Fore.GREEN + "downloading dependency parse sh done..")

    click.echo(Fore.GREEN + "downloading senna for pntl")
    subprocess.call(
        "git clone https://github.com/baojie/senna.git ./pntl/senna".split(),
        shell=True,
        stdout=subprocess.PIPE,
    )


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

        click.echo("\n", sent, "\n")

        sent = sent.split()
        args = "-srl -pos".strip().split()

        click.echo("conll:\n", annotator.get_conll_format(sent, args))

        temp = annotator.get_annoations(sent, dep_parse=True)

        click.echo("dep_parse:\n", temp["dep_parse"])

        click.echo("chunk:\n", temp["chunk"])

        click.echo("pos:\n", temp["pos"])

        click.echo("ner:\n", temp["ner"])

        click.echo("srl:\n", temp["srl"])

        click.echo("syntaxTree:\n", temp["syntax_tree"])

        click.echo("words:\n", temp["words"])

        click.echo("skip gram\n", list(skipgrams(sent, n=3, k=2)))

    else:

        click.echo("\n\nrunning batch process", "\n", "=" * 20, "\n", sent, "\n")

        args = "-srl -pos".strip().split()

        click.echo("conll:\n", annotator.get_conll_format(sent, args))

        click.echo(Fore.BLUE + "CoNLL format is recommented for batch process")


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

    if init:

        download_files()

    main(senna_path, sent, dep_model, batch, stp_dir)
