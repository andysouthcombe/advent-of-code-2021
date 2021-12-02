import pytest
from aoc_day2 import read_input
from aoc_day2 import Submarine

def test_read_input_content():
    directions = read_input('input\\day2_test.txt')
    assert directions[0] == ('forward', 5)
    assert directions[4] == ('down', 8)

def test_read_input_types():
    directions = read_input('input\\day2_test.txt')
    (direction, distance) = directions[1]
    assert isinstance(direction, str)
    assert isinstance(distance, int)

def test_sub_can_move_forward():
    sub = Submarine()
    directions = ('forward', 1)
    sub.move(directions)
    assert sub.horizontal == 1
    assert sub.depth == 0

def test_sub_can_move_up():
    sub = Submarine()
    directions = ('up', 1)
    sub.move(directions)
    assert sub.horizontal == 0
    assert sub.depth == -1

def test_sub_can_move_down():
    sub = Submarine()
    directions = ('down', 2)
    sub.move(directions)
    assert sub.horizontal == 0
    assert sub.depth == 2