from typing import List

from .line import Line

import abc

class Source(metaclass=abc.ABCMeta):
    @property
    @abc.abstractclassmethod
    def lines(self) -> List[Line]:
        pass


class FileSource(Source):
    def __init__(self, file_name: str):
        self.name = file_name
        self.f = open(file_name, "rt")

    @property
    def lines(self):
        for line_num, line in enumerate(self.f.readlines()):
            yield Line.process(self, line_num, line)


class StringSource(Source):
    def __init__(self, name: str, lines: List[str]):
        self.name = name
        self._lines = lines

    @property
    def lines(self):
        for line_num, line in enumerate(self._lines):
            yield Line.process(self, line_num + 1, line)
