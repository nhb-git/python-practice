from abc import ABCMeta, abstractmethod


class Fruit(metaclass=ABCMeta):
    """ 抽象类. """
    @abstractmethod
    def taste(self):
        pass

    @abstractmethod
    def originated(self):
        pass


class Apple:
    """..."""
    def originated(self):
        """..."""
        return 'Central Asia'


fruit = Fruit('apple')
