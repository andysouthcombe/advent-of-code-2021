from aoc_utils import read_file_of_strings
from dataclasses import dataclass

@dataclass
class Octopus:
    def __init__(self, energy) -> None:
        self.energy = int(energy)
    
    def take_step(self):
        self.energy += 1
        if self.energy == 10:
            self.energy = 0


def initialise_octopi_grid(filename):
    initial_octopi = read_file_of_strings(filename)
    octopi_grid = []
    for line in initial_octopi:
        octopus_line = []
        for octopus_energy in line:
            octopus_line.append(Octopus(octopus_energy))
        octopi_grid.append(octopus_line)
    return octopi_grid