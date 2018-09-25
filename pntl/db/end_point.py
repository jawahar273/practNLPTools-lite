# end point is access point of the api

from pntl.db.model import Package
from pntl.db.config import SessionMaker


class EntryPoint:

    """EntryPoint class define as access point
    for the class in `db.model` file.
    """

    def __init__(self, tagged=None):

        self.db = Package
        self.session = SessionMaker()

    def create_table(self):

        from pntl.db.config import Base, engine

        return Base.metadata.create_all(engine)

    def insert(self, tagged=None):

        if not isinstance(tagged, dict) and not tagged:

            ValueError("given value must `dict` with non empty..")

        self.session.add(self.db(**tagged))

    def filter(self):
        # arg will be selected soon..
        pass

    def save(self):

        self.session.commit()

    def roll_back(self):

        self.session.rollback()
