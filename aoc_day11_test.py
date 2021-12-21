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

def test_flash_increments_right_neighbour():
    double_octopus_grid = OctopiGrid([[9, 2]])
    double_octopus_grid.take_step()
    assert double_octopus_grid.get_octopus(1, 0)  == 4

def test_flash_increments_all_neighbours():
    nine_square_octopus_grid = OctopiGrid([[1, 1, 1],
                                            [1, 9, 1],
                                            [1, 1, 1]])
    nine_square_octopus_grid.take_step()
    assert nine_square_octopus_grid.octopi_lines  ==  OctopiGrid([[3, 3, 3],
                                                      [3, 0, 3],
                                                      [3, 3, 3]]).octopi_lines
    
def test_flash_chain_reaction():
    nine_square_octopus_grid = OctopiGrid([[8, 8, 8],
                                            [8, 9, 8],
                                            [8, 8, 8]])
    nine_square_octopus_grid.take_step()
    assert nine_square_octopus_grid.octopi_lines  ==  OctopiGrid([[0, 0, 0],
                                                      [0, 0, 0],
                                                      [0, 0, 0]]).octopi_lines
    