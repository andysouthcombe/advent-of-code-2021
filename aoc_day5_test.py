import pytest

from aoc_day5 import coords, get_all_coords_on_line, grid, line, not_diagonal, read_lines

lines = read_lines('input\\day5_test.txt')
test_grid = grid(lines)

def test_read_lines_correctly():
    assert lines[0] == line(start = coords(x=0,y=9),end = coords(x=5,y=9))
    assert lines[1] == line(start = coords(x=8,y=0),end = coords(x=0,y=8))

def test_line_eq_operator():
    line_1 = line(coords(0,9),coords(5,9))
    line_2 = line(coords(0,9),coords(5,9))
    line_3 = line(coords(0,8),coords(5,9))
    assert line_1 == line_2
    assert line_1 != line_3

def test_line_not_diagonal_for_horiztonal_line():
    assert not_diagonal(line(coords(0,9),coords(5,9))) == True

def test_line_not_diagonal_for_vertical_line():
    assert not_diagonal(line(coords(0,6),coords(0,7))) == True

def test_line_not_diagonal_for_diagonal_line():
    assert not_diagonal(line(coords(0,8),coords(5,9))) == False

def test_grid_returns_non_diagonal_lines():
    expected_grid = grid([line(coords(0,9), coords(5,9)),
        line(coords(9,4), coords(3,4)),
        line(coords(2,2), coords(2,1)),
        line(coords(7,0), coords(7,4)),
        line(coords(0,9), coords(2,9)),
        line(coords(3,4), coords(1,4))])
    assert test_grid.get_non_diagonal_lines() == expected_grid.lines

def test_get_grid_size_works_for_test_grid():
    assert test_grid.get_grid_size(test_grid.get_non_diagonal_lines()) == (coords(0,0) , coords(9,9))

def test_get_all_coords_on_horizontal_line():
    test_line_1 = line(coords(3,4), coords(1,4))
    assert get_all_coords_on_line(test_line_1) == [coords(3,4), coords(2,4), coords(1,4)]

def test_get_all_coords_on_vertical_line():
    test_line_2 = line(coords(7,0), coords(7,4))
    assert get_all_coords_on_line(test_line_2) == [coords(7,0), coords(7,1), coords(7,2), coords(7,3), coords(7,4)]

def test_get_all_coords_on_diagonal_line():
    test_line_3 = line(coords(1,1), coords(3,3))
    test_line_4 = line(coords(9,7), coords(7,9)) 
    print(get_all_coords_on_line(test_line_3))
    assert get_all_coords_on_line(test_line_3) == [coords(1,1), coords(2,2), coords(3,3)]
    assert get_all_coords_on_line(test_line_4) == [coords(9,7), coords(8,8), coords(7,9)]

def test_count_points_with_more_than_one__non_diagonal_line_on_test_grid():
    assert test_grid.count_points_with_multiple_non_diagonal_lines_overlapping() == 5

def test_count_points_with_more_than_one__line_on_test_grid():
    assert test_grid.count_points_with_multiple_lines_overlapping() == 12