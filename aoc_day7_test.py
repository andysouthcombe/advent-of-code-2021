from os import read
import pytest

from aoc_utils import read_one_line_int_file
from aoc_day7 import get_crab_sub_position_range,get_move_cost,get_total_move_cost_to_position,get_cheapest_common_position,get_move_cost_part_2

test_crab_subs = read_one_line_int_file('input\\day7_test.txt')

def test_get_crab_sub_position_range():
    min_position, max_position = get_crab_sub_position_range(test_crab_subs)
    assert (min_position, max_position) == (0, 16)

def test_get_move_cost_positive_move():
    assert get_move_cost(0,3) == 3

def test_get_move_cost_negative_move():
    assert get_move_cost(3,1) == 2

def test_get_total_move_cost_to_position():
    assert get_total_move_cost_to_position(test_crab_subs,1,get_move_cost) == 41

def test_get_cheapest_common_position():
    assert get_cheapest_common_position(test_crab_subs,get_move_cost) == (2, 37)

def test_get_move_cost_part_2():
    assert get_move_cost_part_2(0,1) == 1
    assert get_move_cost_part_2(0,2) == 3
    assert get_move_cost_part_2(2,5) == 6
    assert get_move_cost_part_2(14,5) == 45