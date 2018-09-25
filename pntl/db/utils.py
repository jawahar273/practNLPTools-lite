
from hashlib import md5


def hash_value(value):

    return md5(value.encode()).hexdigest()
