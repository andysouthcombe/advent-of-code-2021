import pytest

from aoc_day10 import get_invalid_closing_character

test_input_valid_1 = '()'
test_input_valid_2 = '()()<>{()}'
test_input_invalid_1 = '(]'
test_input_invalid_2 = '{()()<>()>'


def test_simple_valid_input_returns_none():
    assert get_invalid_closing_character(test_input_valid_1) == None

def test_simple_invalid_input_returns_square_bracket():
    assert get_invalid_closing_character(test_input_invalid_1) == ']'

def test_complex_valid_input_returns_none():
    assert get_invalid_closing_character(test_input_valid_2) == None

def test_complex_valid_input_returns_none():
    assert get_invalid_closing_character(test_input_invalid_2) == '>'