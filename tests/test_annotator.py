from os import getcwd
from os.path import join, split as path_split


from pntl.tools import Annotator


class TestAnnotator:
    def setup(self):

        self.sent = "He created the robot and broke it after making it"
        args = {"senna_dir": self.get_senna_path("pntl", "senna"), "save_all": True}
        self.annotator = Annotator(**args)
        self.process = self.annotator.get_annoations(self.sent, dep_parse=True)

    def get_senna_path(self, *value):

        temp = getcwd()

        return join(temp, *value)

    def test_pos(self):

        assert isinstance(list, self.process["pos"])
