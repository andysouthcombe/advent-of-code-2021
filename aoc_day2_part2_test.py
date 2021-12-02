import pytest
from aoc_day2 import move_sub, SubmarinePart2


def test_sub_can_move_forward_level():
    sub = SubmarinePart2()
    directions = ('forward', 1)
    sub.move(directions)
    assert sub.horizontal == 1
    assert sub.depth == 0
    assert sub.aim == 0

def test_sub_can_aim_down():
    sub = SubmarinePart2()
    directions = ('down', 1)
    sub.move(directions)
    assert sub.horizontal == 0
    assert sub.depth == 0
    assert sub.aim == 1

def test_sub_can_aim_up():
    sub = SubmarinePart2(1,3,5)
    directions = ('up', 2)
    sub.move(directions)
    assert sub.horizontal == 3
    assert sub.depth == 1
    assert sub.aim == 3

def test_sub_moves_when_aimed_down():
    sub = SubmarinePart2(0,0,5)
    directions = ('forward',8)
    sub.move(directions)
    assert sub.horizontal == 8
    assert sub.depth == 40
    assert sub.aim == 5

def test_sub_moves_when_aimed_up():
    sub = SubmarinePart2(10,0,-3)
    directions = ('forward',2)
    sub.move(directions)
    assert sub.horizontal == 2
    assert sub.depth == 4
    assert sub.aim == -3

def test_sub_follows_test_directions():
    sub = SubmarinePart2()
    moved_sub = move_sub(sub,'input\\day2_test.txt')
    assert moved_sub.horizontal == 15
    assert moved_sub.depth == 60