from os import getcwd
from os.path import join, split as path_split


from pntl.tools import Annotator


class TestAnnotator:
    def __init__(self):
        self.sent = "He created the robot and broke it after making it"
        args = {"senna_dir": self.get_senna_path("pntl", "senna")}
        self.annotator = Annotator(**args)
        self.process = self.annotator.get_annoations(sent, dep_parse=True)

    def get_senna_path(self, *value):

        temp = path_split(getcwd())[0]

        return join(temp, *value)

    def test_pos(self):

        assert isinstance(list, self.process["pos"])
