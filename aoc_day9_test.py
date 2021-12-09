import pytest

from aoc_day9 import get_neighbour_square_values, read_numbers
test_numbers = read_numbers('input\\day9_test.txt')

def test_read_numbers_ok():
    assert len(test_numbers) == 5
    assert len(test_numbers[0]) == 10

def test_find_neighbours_middle_square():
    assert get_neighbour_square_values(test_numbers, 1,1) == ['1','8','8','3']
