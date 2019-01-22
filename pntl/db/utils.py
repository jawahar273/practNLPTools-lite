from os import getenv
from importlib import import_module

try:

    import ujson as json

except ImportError:

    import json


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

    return json.loads(getenv(value, default))


def import_class(value):
    """Import the given class based on string.
    :param value: path of the class
    :type value: str
    :returns: class object
    :rtype: Object
    """

    value, class_name = value.rsplit(".", 1)
    module = import_module(value)

    return getattr(module, class_name)


def pntl_hash(to_hex):
    """
    As the name suggest it wokring based configuration of
    the user but the default hash string is :py:class:`hashlib.md5` of
    standard libery
    """
    hash_ = import_class(env_str("HASH_CLASS", "hashlib.md5"))

    return hash_(to_hex.encode()).hexdigest()[: env_int("HASH_VALUE_LEN")]
