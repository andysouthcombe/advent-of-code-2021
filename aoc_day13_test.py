from os import read
import pytest
from aoc_day13 import fold_on_axis, extract_points_and_folds, print_points
from aoc_utils import read_file_of_strings

def test_folds_3x1_grid():
    input_points = [(2,0)]
    expected_points = [(0,0)]
    assert fold_on_axis(input_points,'x',1) == expected_points

def test_folds_1x3_grid():
    input_points = [(0,2)]
    expected_points = [(0,0)]
    assert fold_on_axis(input_points,'y',1) == expected_points

def test_does_not_fold_points_before_x_axis():
    input_points = [(1,0)]
    expected_points = [(1,0)]
    assert fold_on_axis(input_points,'x',2) == expected_points

def test_does_not_fold_points_before_y_axis():
    input_points = [(0,1)]
    expected_points = [(0,1)]
    assert fold_on_axis(input_points,'y',2) == expected_points

def test_dedupes_points_that_overlap_x_fold():
    input_points = [(1,0), (3,0)]
    expected_points = [(1,0)]
    assert fold_on_axis(input_points,'x', 2) == expected_points

def test_dedupes_points_that_overlap_y_fold():
    input_points = [(1,1), (1,3)]
    expected_points = [(1,1)]
    assert fold_on_axis(input_points,'y', 2) == expected_points

def test_folds_example_grid():
    points, input_folds = extract_points_and_folds(read_file_of_strings('input\\day13_test.txt'))
    for axis, line in input_folds:
        points = fold_on_axis(points, axis, line)
    print_points(points)
    assert len(points) == 16