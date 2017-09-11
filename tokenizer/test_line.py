import pytest

from tokenizer import StringSource


class TestLineProessing:
    def test_one(self):
        source = StringSource(
            "test",
            ["one"]
        )
        lines = list(source.lines)
        assert lines
        assert len(lines) == 1
        line = lines[0]
        assert line.source == source
        assert line.num == 1
        tokens = line.tokens
        assert tokens
        assert len(tokens) == 1
        token = tokens[0]
        assert token.line == line
        assert token.pos == 0
        assert token.text == 'one'

    def test_some_text(self):
        source = StringSource(
            "test_some_text",
            ["one two"]
        )
        lines = list(source.lines)
        assert len(lines) == 1
        line = lines[0]
        tokens = line.tokens
        assert len(tokens) == 2
        token1, token2 = tokens
        assert token1.pos == 0
        assert token1.text == "one"
        assert token2.pos == 4
        assert token2.text == "two"

    def test_with_spaces(self):
        source = StringSource(
            "test_spaces",
            ["   one  three     "]
        )
        lines = list(source.lines)
        assert len(lines) == 1
        line = lines[0]
        tokens = line.tokens
        assert len(tokens) == 2
        token1, token2 = tokens
        assert token1.pos == 3
        assert token1.text == "one"
        assert token2.pos == 8
        assert token2.text == "three"

    def test_empty(self):
        source = StringSource(
            "test_empty",
            [""]
        )
        lines = list(source.lines)
        assert len(lines) == 1
        assert len(lines[0].tokens) == 0


