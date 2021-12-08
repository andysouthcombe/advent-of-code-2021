from os import read
import pytest

from aoc_day6 import day_pass, read_file

test_fishes = read_file('input\\day6_test.txt')

def test_file_read_ok():
    assert len(test_fishes) == 5

def timer_decrements_number_greater_than_1():
    assert day_pass(test_fishes)[0] == 2