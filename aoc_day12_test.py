from os import read
from aoc_utils import read_file_of_strings
from aoc_day12 import parse_route_list, get_routes_from_cave
import pytest

route_list = parse_route_list('input\\day12_test.txt')

def test_parses_route_list():
    assert len(route_list) == 14

def test_get_routes_from_cave():
    expected_routes = [('A','c'), ('A','b'), ('A', 'end'), ('A','start')]
    assert expected_routes == get_routes_from_cave('A',route_list)