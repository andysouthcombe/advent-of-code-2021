from os import read


class heightmap:
    def __init__(self,squares):
        self.squares = squares
        self.max_y = len(squares) - 1
        self.max_x = len(squares[0]) - 1
    
    def get_neighbour_square_values(self, y, x):
        neighbours = []
        if self.has_above(y):
            neighbours.append(int(self.squares[y-1][x]))
        if self.has_right(x):
            neighbours.append(int(self.squares[y][x+1]))
        if self.has_below(y):
            neighbours.append(int(self.squares[y+1][x]))
        if self.has_left(x):
            neighbours.append(int(self.squares[y][x-1]))
        return neighbours
    
    def has_above(self, y):
        return y > 0

    def has_below(self, y):
        return y < self.max_y
    
    def has_left(self, x):
        return x > 0
        
    def has_right(self, x):
        return x < self.max_x
    
    def find_low_points_and_risk_levels(self):
        low_points = []
        risk_levels = []
        for y, row in enumerate(self.squares):
            for x, square in enumerate(row):
                square_number = int(square)
                neighbour_values = self.get_neighbour_square_values(y, x)
                if square_number < min(neighbour_values):
                    low_points.append((y, x))
                    risk_levels.append(square_number + 1)
        return risk_levels, low_points


def read_numbers(filename):
    with open(filename,'r') as f:
        return [line.rstrip() for line in f.readlines()]


if __name__ == '__main__':
    full_heightmap = heightmap(read_numbers('input\\day9.txt'))
    print(f'Risk levels are {sum(full_heightmap.find_low_points_and_risk_levels()[0])}')
