from typing import List, Iterator

from .token import Token


class Line:
    def __init__(self, source:"Source", line_num: int, tokens: List[Token]):
        self.source = source
        self.num = line_num
        self.tokens = tokens
        self._attach_tokens()

    def _attach_tokens(self):
        for token in self.tokens:
            token.line = self

    @classmethod
    def _tokenize(cls, line: str) -> Iterator[Token]:
        text = ""
        pos = 0
        for ch in line:
            if ch.isspace():
                if text.strip():
                    yield Token(None, pos - len(text), text.strip())
                    text = ""
            else:
                text += ch
            pos += 1
        if text.strip():
            yield Token(None, pos - len(text), text.strip())

    @classmethod
    def process(cls, source: "Source", line_num: int, line: str,) -> "Line":
        return Line(source, line_num, list(cls._tokenize(line)))
