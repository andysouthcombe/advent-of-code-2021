import pytest

from aoc_day5 import coords, line, not_diagonal, read_lines
lines = read_lines('input\\day_5_test.txt')

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