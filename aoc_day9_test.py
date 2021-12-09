import pytest

from aoc_day9 import read_numbers
test_numbers = read_numbers('input\\day9_test.txt')

def test_read_numbers_ok():
    assert len(test_numbers) == 5
    assert len(test_numbers[0]) == 10