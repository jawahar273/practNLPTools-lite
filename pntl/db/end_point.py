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

from sqlalchemy.exc import IntegrityError

from pntl.db.config import SessionMaker
from pntl.db.utils import import_class, env_str

package = "pntl.db.model.{}".format(env_str("DB_CLASS"))


class EntryPoint:

    """EntryPoint class define as access point
    for the class in `db.model` file.

    """

    def __init__(self):

        self.db = import_class(package)
        self.session = SessionMaker()
        self.create_table()

    def create_table(self):
        """This method create table in
        database if it exit then it simply
        omittes.

        :returns: it create the engine.
        :rtype: NoneType
        """
        from pntl.db.config import Base, engine

        return Base.metadata.create_all(engine)

    def insert(self, tagged=None):
        """Adding the value into  the database
        with the session of sqlalchme.

        :param dicit tagged: tagged value from SENNA
        """
        if not isinstance(tagged, dict) and not tagged:

            ValueError("given value must `dict` with non empty..")

        tagged["words"] = " ".join(tagged["words"])

        try:

            self.session.add(self.db(**tagged))

        except IntegrityError as e:
            print("duplicate sentence")

    def filter(self):
        # arg will be selected soon..
        # In RoadMap
        raise NotImplementedError("This function has not been implemented")

    def save(self):

        self.session.commit()

    def roll_back(self):

        self.session.rollback()
