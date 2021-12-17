import pytest

from aoc_day11 import OctopiGrid, initialise_octopi_grid
test_grid = initialise_octopi_grid('input\\day11_test.txt')

def test_grid_read_ok():
    assert test_grid.octopi_lines[9] == [5, 2, 8, 3, 7, 5, 1, 5, 2, 6]

def test_get_octopi():
    assert test_grid.get_octopus(0,2)  == 5
    assert test_grid.get_octopus(8,9)  == 2

def test_take_step_increases_energy():
    new_grid = test_grid
    new_grid.take_step()
    assert test_grid.get_octopus(8,9)  == 3

def test_take_step_flashes_at_9():
    single_octopus_grid = OctopiGrid([[9]])
    single_octopus_grid.take_step()
    assert single_octopus_grid.get_octopus(0, 0)  == 0