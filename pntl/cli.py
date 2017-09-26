# -*- coding: utf-8 -*-

"""Console script for practnlptools_lite."""

import click

from pntl.tools import Annotator
from pntl.utils import skipgrams

from colorama import Fore, init
init(autoreset=True)


@click.command()
@click.option('-SA', '--senna_path', help='Set the direction of senna.',
              type=click.Path(exists=True))
@click.option('-S', '--sent', help='Testing sentense to passed in senna.',
              type=str, default='')
@click.option('-DM', '--dep_model',
              help='Stanford dependency parser model location.', type=str)
@click.option('-B', '--batch',
              type=click.BOOL, help='Batch process.')
@click.option('-SD', '--stp_dir',
              type=str, help='Location of stanford-parser.jar file.')
# @click.option('-h', '--help',
#               help='Show this message and exit.')
def test(senna_path="", sent="", dep_model="", batch=False, stp_dir=""):
    """please replace the path of yours environment(accouding to OS path)

    :param str senna_path: path for senna location
    :param str dep_model: stanford dependency parser model location
    :param str or list sent: the sentense to process with Senna
    :param bool batch: makeing as batch process with one or more sentense
       passing
    :param str stp_dir: location of stanford-parser.jar file
    """
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
        print(Fore.BLUE + "CoNLL format is recommented for batch process")


if __name__ == "__main__":
    try:
        test()
    except Exception as e:
        print(Fore.RED + e,
              "\n\nTo know about more issue to this link"
              " https://github.com/jawahar273/practNLPTools-lite/wiki")

