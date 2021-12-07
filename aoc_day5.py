from dataclasses import dataclass
from typing import List
from collections import Counter

@dataclass(frozen=True)
class coords:
    x: int
    y: int

@dataclass
class line:
    start: coords
    end: coords

def get_coord_step(start,end):
    if start > end:
        return -1
    return 1

def get_all_coords_on_line(line):
        x_step = get_coord_step(line.start.x, line.end.x)
        y_step = get_coord_step(line.start.y, line.end.y)
        coords_on_line = []
        for x in range(line.start.x, line.end.x + x_step, x_step):
            for y in range(line.start.y, line.end.y + y_step, y_step):
                coords_on_line.append(coords(x,y))
        return coords_on_line
            
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

    def count_points_with_multiple_non_diagonal_lines_overlapping(self):
        coords_crossed_by_lines = []
        lines = self.get_non_diagonal_lines()
        for line in lines:
            coords_on_line = get_all_coords_on_line(line)
            for coord in coords_on_line:
                coords_crossed_by_lines.append(coord)
        return len([coord for (coord, count) in list(Counter(coords_crossed_by_lines).most_common()) if count > 1])

def read_lines(filename):
    with open(filename,'r') as f:
        raw_lines = [raw_line.rstrip().split(' -> ') for raw_line in f.readlines()]
        split_coords = [(raw_line_start.split(',')[0], raw_line_start.split(',')[1], raw_line_end.split(',')[0], raw_line_end.split(',')[1])  for raw_line_start, raw_line_end in raw_lines]
        return [line(coords(int(start_x),int(start_y)), coords(int(end_x),int(end_y)) ) for start_x, start_y,end_x,end_y in split_coords]
        