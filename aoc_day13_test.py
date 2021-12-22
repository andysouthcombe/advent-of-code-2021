import pytest
from aoc_day13 import fold_on_axis

def test_folds_3x1_grid():
    input_points = [(2,0)]
    expected_points = [(0,0)]
    assert fold_on_axis(input_points,'x',1) == expected_points

# def test_folds_1x3_grid():
#     input_points = [(2,0)]
#     expected_points = [(0,0)]
#     assert fold_on_axis(input_points,'y',1) == expected_points
