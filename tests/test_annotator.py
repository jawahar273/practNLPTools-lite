from os import getcwd
from os.path import join, split as path_split


from pntl.tools import Annotator


class TestAnnotator:
    def setup(self):

        self.sent = "PgAdmin is the leading Open Source management tool for Postgres, the world’s most advanced Open Source database."
        args = {"senna_dir": self.get_senna_path("pntl", "senna"), "save_all": True}
        self.annotator = Annotator(**args)
        self.process = self.annotator.get_annoations(self.sent, dep_parse=True)
        print(self.process["chumk"])

    def get_senna_path(self, *value):

        temp = getcwd()

        return join(temp, *value)
