from aoc_utils import read_file_of_strings

class OctopiGrid:
    def __init__(self, octopi_lines):
        self.octopi_lines = octopi_lines

    def get_octopus(self, x, y):
        return int(self.octopi_lines[y][x])

def initialise_octopi_grid(filename):
    return  OctopiGrid(read_file_of_strings(filename))