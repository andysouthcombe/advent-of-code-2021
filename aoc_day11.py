from aoc_utils import read_file_of_strings
from dataclasses import dataclass

@dataclass
class OctopiGrid:
    def __init__(self, octopi_lines):
        self.octopi_lines = octopi_lines

    def get_octopus(self, x, y):
        return int(self.octopi_lines[y][x])
    
    def increment_octopus(self, x, y):
        self.octopi_lines[y][x] += 1
    
    def flash_octopus(self, x, y):
        self.octopi_lines[y][x] = 0
    
    def check_if_neighbour_flashed(self, x, y, flashed_x, flashed_y):
        if abs(x - flashed_x) <=1 and abs(y - flashed_y) <= 1:
            return True
        return False
    
    def take_step(self):
        flashed_octopi = []
        flashing_queue = []
        for y, octopi_line in enumerate(self.octopi_lines):
            for x in range(0, len(octopi_line)):
                self.increment_octopus(x, y)
                if self.get_octopus(x, y) > 9:
                    self.flash_octopus(x, y)
                    flashed_octopi.append((x, y))
                    flashing_queue.append((x, y))
        while flashing_queue:
            flashed_x, flashed_y = flashing_queue.pop()
            for y, octopi_line in enumerate(self.octopi_lines):
                for x in range(0, len(octopi_line)):
                    if self.check_if_neighbour_flashed(x, y, flashed_x,flashed_y) and (x,y) not in flashed_octopi:
                        self.increment_octopus(x, y)
                        if self.get_octopus(x,y) > 9:
                            self.flash_octopus(x, y)
                            flashed_octopi.append((x, y))
                            flashing_queue.append((x,y))
        return len(flashed_octopi)
        
    def take_number_of_steps(self, steps):
        flashed_count = []
        for i in range(0,steps):
            flashed_count.append(self.take_step())
        print(self.octopi_lines)
        return sum(flashed_count)
    
    def take_steps_until_all_flash(self):
        octopi_count = len(self.octopi_lines) * len(self.octopi_lines[0])
        flashed_count = 0
        step_count = 0
        while flashed_count < octopi_count:
            flashed_count = self.take_step()
            step_count += 1
        return step_count
                

def initialise_octopi_grid(filename):
    raw_grid = read_file_of_strings(filename)
    octopi_grid = []
    for octopi_line in raw_grid:
        octopi_grid.append([int(octopus) for octopus in octopi_line])
    return  OctopiGrid(octopi_grid)


if __name__ == '__main__':
    test_octopi_grid = initialise_octopi_grid('input\\day11_test.txt')
    number_of_flashes = test_octopi_grid.take_number_of_steps(100)
    print(f'After 100 steps for part 1 test grid we have {number_of_flashes} flashes')
    octopi_grid = initialise_octopi_grid('input\\day11.txt')
    number_of_flashes = octopi_grid.take_number_of_steps(100)
    print(f'After 100 steps for part 1 we have {number_of_flashes} flashes')

    test_octopi_grid_part_2 = initialise_octopi_grid('input\\day11_test.txt')
    number_of_flashes = test_octopi_grid_part_2.take_steps_until_all_flash()
    print(f'We needed {number_of_flashes} for test grid before all flashed together')

    octopi_grid_part_2 = initialise_octopi_grid('input\\day11.txt')
    number_of_flashes = octopi_grid_part_2.take_steps_until_all_flash()
    print(f'We needed {number_of_flashes} for real grid before all flashed together')
    