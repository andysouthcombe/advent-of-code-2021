from dataclasses import dataclass
from typing import List

@dataclass
class coords:
    x: int
    y: int

@dataclass
class line:
    start: coords
    end: coords

def not_diagonal(line):
    return line.start.x == line.end.x or line.start.y == line.end.y

@dataclass
class grid:
    lines: List
    
    def get_non_diagonal_lines(self):
        return list(filter(not_diagonal, self.lines))
    
    def get_grid_size(self, lines):
        x_coords = [line.start.x for line in lines] + [line.end.x for line in lines]
        y_coords = [line.start.y for line in lines] + [line.end.y for line in lines]
        return coords(min(x_coords),min(y_coords)), coords(max(x_coords), max(y_coords))

def read_lines(filename):
    with open(filename,'r') as f:
        raw_lines = [raw_line.rstrip().split(' -> ') for raw_line in f.readlines()]
        split_coords = [(raw_line_start.split(',')[0], raw_line_start.split(',')[1], raw_line_end.split(',')[0], raw_line_end.split(',')[1])  for raw_line_start, raw_line_end in raw_lines]
        return [line(coords(int(start_x),int(start_y)), coords(int(end_x),int(end_y)) ) for start_x, start_y,end_x,end_y in split_coords]
        