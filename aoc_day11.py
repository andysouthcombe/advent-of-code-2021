from aoc_utils import read_file_of_strings

class OctopiGrid:
    def __init__(self, octopi_lines):
        self.octopi_lines = octopi_lines

    def get_octopus(self, x, y):
        return int(self.octopi_lines[y][x])
    
    def increment_octopus(self, x, y):
        self.octopi_lines[y][x] += 1
    
    def flash_octopus(self, x, y):
        self.octopi_lines[y][x] = 0
    
    def take_step(self):
        for y, octopi_line in enumerate(self.octopi_lines):
            for x in range(0, len(octopi_line)):
                self.increment_octopus(x, y)
                if self.get_octopus(x, y) > 9:
                    self.flash_octopus(x, y)
                
                

def initialise_octopi_grid(filename):
    raw_grid = read_file_of_strings(filename)
    octopi_grid = []
    for octopi_line in raw_grid:
        octopi_grid.append([int(octopus) for octopus in octopi_line])
    return  OctopiGrid(octopi_grid)