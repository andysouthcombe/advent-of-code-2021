from aoc_utils import read_file_of_strings
from dataclasses import dataclass

def parse_route_list(filename):
    raw_list = [route.split('-') for route in read_file_of_strings(filename)]
    return [(start, end) for start, end in raw_list] + [(end, start) for start, end in raw_list ]
    
def get_routes_from_cave(cave, route_list):
    return [route[1] for route in route_list if cave == route[0]]

def is_cave_small(cave):
    return cave.islower()

def find_paths(route_list):
    path_list = []
    current_location = 'start'
    next_steps = get_routes_from_cave('start', route_list)
