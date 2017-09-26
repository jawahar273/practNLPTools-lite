from __future__ import generators, print_function, unicode_literals
from itertools import chain, combinations

# from nltk.util import ngrams
from colorama import Fore, init
init(autoreset=True)

def pad_sequence(seq, n, pad_left=False, pad_right=False, pad_sym=None):
    if pad_left:
        sequence = chain((pad_sym,) * (n - 1), seq)
    if pad_right:
        sequence = chain(seq, (pad_sym,) * (n - 1))
    return sequence


def skipgrams(seq, n=2, k=1, pad_left=False, pad_right=False, pad_sym=None):
    sequence_length = len(seq)
    sequence = iter(seq)
    sequence = pad_sequence(seq, n, pad_left, pad_right, pad_sym)
    if sequence_length + pad_left + pad_right < k:
        raise Exception("The length of sentence + padding(s) < skip")

    if n < k:
        raise Exception(Fore.RED + "Degree of Ngrams (n)"
                        "needs to be bigger than skip (k)")

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

