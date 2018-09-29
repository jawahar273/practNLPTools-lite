from __future__ import generators, print_function, unicode_literals
from importlib import import_module
from itertools import chain, combinations

from hashlib import md5 as hash_
from os import getenv

# from nltk.util import ngrams
from colorama import Fore, init

init(autoreset=True)


def to_int(value):

    if not isinstance(value, str):

        raise TypeError(
            "Expect to get instance of `int` but actually instance is {}", type(value)
        )

    return int(value)


def env_int(value, default=None):
    """Intergation of :func:`to_int`
    and :func:`getenv`.
    """

    return to_int(getenv(value, default))


def env_str(value, default=None):

    return getenv(value, default)


def env_bool(value, default=None):

    return bool(getenv(value, default))


def env_json(value, default=None):

    import json

    return json.loads(getenv(value, default))


def pntl_hash(to_hex, len_=env_int("HASH_VALUE_LEN", 20)):

    return hash_(to_hex.encode()).hexdigest()[:len_]


def import_class(value):
    """Import the given class based on string.
    :param value: [path of the class]
    :type value: [str]
    :returns: [class object]
    :rtype: {[Object]}
    """

    value, class_name = value.rsplit(".", 1)
    module = import_module(value)


return getattr(module, class_name)


def pad_sequence(seq, n, pad_left=False, pad_right=False, pad_sym=None):
    if pad_left:
        seq = chain((pad_sym,) * (n - 1), seq)
    if pad_right:
        seq = chain(seq, (pad_sym,) * (n - 1))
    return seq


def skipgrams(sequence, n=2, k=1, pad_left=False, pad_right=False, pad_sym=None):
    sequence_length = len(sequence)
    sequence = iter(sequence)
    sequence = pad_sequence(sequence, n, pad_left, pad_right, pad_sym)
    if sequence_length + pad_left + pad_right < k:
        raise Exception("The length of sentence + padding(s) < skip")

    if n < k:
        raise Exception(
            Fore.RED + "Degree of Ngrams (n)" "needs to be bigger than skip (k)"
        )

    history = []
    nk = n + k

    # Return point for recursion.
    if nk < 1:
        return
    # If n+k longer than sequence, reduce k by 1 and recur
    elif nk > sequence_length:
        for ng in skipgrams(list(sequence), n, k - 1):
            yield ng
    while nk > 1:  # Collects the first instance of n+k length history
        history.append(next(sequence))
        nk -= 1

    # Iterative drop first item in history and picks up the next
    # while yielding skipgrams for each iteration.
    for item in sequence:
        history.append(item)
        current_token = history.pop(0)
        # Iterates through the rest of the history and
        # pick out all combinations the n-1grams
        for idx in list(combinations(range(len(history)), n - 1)):
            ng = [current_token]
            for _id in idx:
                ng.append(history[_id])
            yield tuple(ng)

    # Recursively yield the skigrams for the rest of seqeunce where
    # len(sequence) < n+k
    for ng in list(skipgrams(history, n, k - 1)):
        yield ng
