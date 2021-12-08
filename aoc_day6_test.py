from os import read
import pytest

from aoc_day6 import read_file

test_numbers = read_file('input\\day6_test.txt')

def test_file_read_ok():
    assert len(test_numbers) == 5