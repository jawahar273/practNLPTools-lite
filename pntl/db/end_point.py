# end point is access point of the api

from pntl.db.model import Package


class EndPoint:

    '''EndPoint class define as access point
    for the class in `db.model` file.
    '''

    def __init__(self, tagged=None):

        if not isinstance(tagged, dict) and not tagged:

            ValueError('given value must `dict` with non empty..')

        self.db = Package(tagged)
