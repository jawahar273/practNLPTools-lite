from abc import ABC, abstractmethod


class AbstractEngine(ABC):
    """This is a abstract class for the
    search engine module.
    """

    def __not_implemented(self):

        raise NotImplementedError("Child class has not been implemented")

    @abstractmethod
    def query(self, *args, **kwargs):

        return self.__not_implemented()
