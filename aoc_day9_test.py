import pytest

from aoc_day9 import heightmap, read_numbers
test_heightmap = heightmap(read_numbers('input\\day9_test.txt'))

def test_read_numbers_ok():
    assert len(test_heightmap.squares) == 5
    assert len(test_heightmap.squares[0]) == 10

def test_find_neighbours_middle_square():
    assert heightmap.get_neighbour_square_values(test_heightmap, 1,1) == [1,8,8,3]

def test_find_neighbours_for_top_middle_square():
    assert heightmap.get_neighbour_square_values(test_heightmap,0,1) == [9,9,2]

def test_find_neighbours_for_bottom_middle_square():
    assert heightmap.get_neighbour_square_values(test_heightmap,4,8) == [8,8,6]