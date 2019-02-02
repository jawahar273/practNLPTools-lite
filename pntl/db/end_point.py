"""
EntryPoint will be act as interface
medium for acessing the db api (sqlalchemy).

.. warning::

    Please install `SQL Database driver` for python
    manully `driver link <https://docs.sqlalchemy.org/en/latest/dialects/>`_

Hash Value's
-------------

Hash will be saved on to the database based
on the hash value return by the function which selected
by you.
As the hash function may depends on the system's
property, such as seed values may diffrent from
system to system.
"Is it possible to distribute the db backup for another's system
without any problem?"
It is highly recommend not to make any dependency
based on hash value (such as generation).

.. note::

    But using standard libery of python
    it possible to get same result on
    all system.


.. todo::

    [In progress]
    Change the class name in the .env to `DistPackage` to
    accessing the table which is related to the elasticserach
    stores and set bash for the enviroment variable
    `ELASTICSEARCH_HOST`
    (follow `link <http://elasticsearch-dsl.readthedocs.io/>`_).

"""
import logging

logging.basicConfig(
    filename="db.log", filemode="w", format="%(name)s - %(levelname)s - %(message)s"
)

from sqlalchemy.exc import IntegrityError
from sqlalchemy import event

from pntl.db.config import SessionMaker
from pntl.db.utils import import_class, env_str
from pntl.db.model import DuplicateAnomaly


class EntryPoint:

    """EntryPoint class define as access point
    for the class in :py:class:`pntl.db.model` file.

    """

    def __init__(self):

        self.db = import_class(
            f"{env_str('DB_CLASS', default='pntl.db.model.Package')}"
        )
        self.session = SessionMaker()
        self.create_table()
        logging.warning("Don't forget to call `save` method")

    def create_table(self):
        """This method create table in
        database if it exit then it simply
        omittes.

        :returns: it create the engine.
        :rtype: NoneType

        .. note::
            * add filter function.
        """
        from pntl.db.config import Base, engine

        return Base.metadata.create_all(engine)

    def insert(self, tagged=None):
        """Adding the value into  the database
        with the session of sqlalchme.

        :param dicit tagged: tagged value from SENNA

        # quick ref: json schema validations.
        """
        if not isinstance(tagged, dict) and not tagged:

            ValueError("given value must `dict` with non empty..")

        tagged["words"] = " ".join(tagged["words"])
        self.session.add(self.db(**tagged))

    def search(self, search_text):

        hash_value = self.db.filter(search_text)
        temp = self.session.query(self.db).filter(self.db.hash_str == hash_value)
        temp_len = temp.count()

        if temp_len == 1:

            # quick ref: need to add custome dict model.
            return temp[0].__dict__

        else:

            raise DuplicateAnomaly(msg="May be Out-of-box write has been accessed")

    def save(self):

        try:

            self.session.commit()

        except IntegrityError as e:

            logging.warning(f"{e}")

    def roll_back(self):

        self.session.rollback()
