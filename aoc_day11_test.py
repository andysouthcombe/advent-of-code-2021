import pytest

from aoc_utils import read_file_of_strings
from aoc_day11 import Octopus, initialise_octopi_grid
test_grid = read_file_of_strings('input\\day11_test.txt')

def test_grid_read_ok():
    assert test_grid[9] == '5283751526'

def test_octopi_grid_set_up_ok():
    octopi_grid = initialise_octopi_grid('input\\day11_test.txt')
    assert octopi_grid[0][0]  == Octopus(5)
    assert octopi_grid[9][9]  == Octopus(6)
