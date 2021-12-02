import pytest
from aoc_day2 import move_sub, SubmarinePart2


def test_sub_can_move_forward_level():
    sub = SubmarinePart2()
    directions = ('forward', 1)
    sub.move(directions)
    assert sub.horizontal == 1
    assert sub.depth == 0
    assert sub.aim == 0


# def test_sub_follows_test_directions():
#     sub = SubmarinePart1()
#     moved_sub = move_sub(sub,'input\\day2_test.txt')
#     assert moved_sub.horizontal == 15
#     assert moved_sub.depth == 10