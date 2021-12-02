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

# def test_sub_follows_test_directions():
#     sub = SubmarinePart1()
#     moved_sub = move_sub(sub,'input\\day2_test.txt')
#     assert moved_sub.horizontal == 15
#     assert moved_sub.depth == 10