import pytest
from aoc_day2 import read_input

def test_read_input_content():
    directions = read_input('input\\day2_test.txt')
    assert directions[0] == ('forward', 5)
    assert directions[4] == ('down', 8)

def test_read_input_types():
    directions = read_input('input\\day2_test.txt')
    (direction, distance) = directions[1]
    assert isinstance(direction, str)
    assert isinstance(distance, int)