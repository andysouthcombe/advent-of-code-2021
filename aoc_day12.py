from aoc_utils import read_file_of_strings
from dataclasses import dataclass

def parse_routes_list(filename):
    raw_list = [route.split('-') for route in read_file_of_strings(filename)]
    return [(start, end) for start, end in raw_list] + [(end, start) for start, end in raw_list ]
    
