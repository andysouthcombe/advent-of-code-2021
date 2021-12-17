import pytest

from aoc_day11 import initialise_octopi_grid
test_grid = initialise_octopi_grid('input\\day11_test.txt')

def test_grid_read_ok():
    assert test_grid.octopi_lines[9] == '5283751526'

def test_get_octopi():
    assert test_grid.get_octopus(0,2)  == 5
    assert test_grid.get_octopus(8,9)  == 2