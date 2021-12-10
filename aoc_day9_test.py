import pytest

from aoc_day9 import heightmap, read_numbers
test_heightmap = heightmap(read_numbers('input\\day9_test.txt'))

def test_read_numbers_ok():
    assert len(test_heightmap.squares) == 5
    assert len(test_heightmap.squares[0]) == 10

def test_find_neighbours_middle_square():
    assert test_heightmap.get_neighbour_square_values(1,1) == [1,8,8,3]

def test_find_neighbours_for_top_middle_square():
    assert test_heightmap.get_neighbour_square_values(0,1) == [9,9,2]

def test_find_neighbours_for_bottom_middle_square():
    assert test_heightmap.get_neighbour_square_values(4,8) == [8,8,6]

def test_find_neighbours_for_left_square():
   assert test_heightmap.get_neighbour_square_values(2,0) == [3,8,8]

def test_find_neighbours_for_right_square():
   assert test_heightmap.get_neighbour_square_values(0,9) == [1,1]

def test_find_low_points():
    assert test_heightmap.find_low_points_and_risk_levels()[0] == [2, 1, 6, 6]