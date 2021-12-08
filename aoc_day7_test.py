from os import read
import pytest

from aoc_utils import read_one_line_int_file
from aoc_day7 import get_crab_sub_position_range

test_crab_subs = read_one_line_int_file('input\\day7_test.txt')

def test_get_crab_sub_position_range():
    min_position, max_position = get_crab_sub_position_range(test_crab_subs)
    assert (min_position, max_position) == (0, 16)

