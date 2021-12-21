from os import read
from aoc_utils import read_file_of_strings
from aoc_day12 import parse_routes_list
import pytest

test_map_raw = read_file_of_strings('input\\day12_test.txt')

def test_parses_route_list():
    route_list = parse_routes_list('input\\day12_test.txt')
    print(route_list)
    assert len(route_list) == 14

