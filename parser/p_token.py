import abc
import re

from tokenizer import Token

class PToken(metaclass=abc.ABCMeta):
    regexpr = r""

    def __init__(self, token: Token, match):
        self.token = token
        self.groups = match.groups()
        self._process()

    @abc.abstractmethod
    def _process(self):
        pass

    @classmethod
    def check(cls, token: Token):
        if hasattr(cls, "_r"):
            cls._r = re.compile(cls.regexpr)
        match = cls._r.fullmatch(token.text)
        if match:
            return cls(token)


class Number(PToken):
    regexpr = r"(-)?(\d*)"

    def _process(self):
        self.value = int(self.groups[1])
        if self.groups[0] is not None:
            self.value = - self.value