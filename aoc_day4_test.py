import pytest

from aoc_day4 import read_numbers

numbers = read_numbers('input\\day_4_test_numbers.txt')

def test_numbers_read_in_ok():
    assert numbers[0] == '7'
    assert len(numbers) == 27