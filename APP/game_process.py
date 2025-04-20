from abc import ABC, abstractmethod


class GameProcess(ABC):
    @abstractmethod
    def tick(self, *args):
        ...
