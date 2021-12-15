import pytest

from aoc_utils import read_file_of_strings, read_one_line_int_file

def test_file_read_one_line_int_file():
    int_list = read_one_line_int_file('input\\day6_test.txt')
    assert len(int_list) == 5
    assert int_list[2] == 3

def test_file_of_strings_read():
    string_list = read_file_of_strings('input\\day10_test.txt')
    assert string_list[9] == '<{([{{}}[<[[[<>{}]]]>[]]'