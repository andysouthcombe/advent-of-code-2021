from collections import deque

class heightmap:
    def __init__(self,squares):
        self.squares = squares
        self.max_y = len(squares) - 1
        self.max_x = len(squares[0]) - 1
    
    def get_neighbour_square_positions(self, y, x):
        neighbours = []
        if self.has_above(y):
            neighbours.append((y-1, x))
        if self.has_right(x):
            neighbours.append((y, x+1))
        if self.has_below(y):
            neighbours.append((y+1, x))
        if self.has_left(x):
            neighbours.append((y, x-1))
        return neighbours
    
    def get_neighbour_square_values(self, neighbours):
        square_values = []
        for y, x in neighbours:
            square_values.append(int(self.squares[y][x]))
        return square_values

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
                neighbours = self.get_neighbour_square_positions(y, x)
                neighbour_values = self.get_neighbour_square_values(neighbours)
                if square_number < min(neighbour_values):
                    low_points.append((y, x))
                    risk_levels.append(square_number + 1)
        return low_points, risk_levels
    
    def find_basin(self, low_point_y, low_point_x):
        basin = []
        visited = set()
        queue = deque([(low_point_y, low_point_x)])
        
        while queue:
            (y, x) = queue.pop()

            if (y, x) in visited:
                continue
            else:
                visited.add((y, x))
                if self.squares[y][x] != '9':
                    basin.append((y, x))
                    queue.extend([(y_neighbour, x_neighbour) for (y_neighbour, x_neighbour) in self.get_neighbour_square_positions(y, x) if (y_neighbour, x_neighbour) not in visited])

        return basin




def read_numbers(filename):
    with open(filename,'r') as f:
        return [line.rstrip() for line in f.readlines()]


if __name__ == '__main__':
    full_heightmap = heightmap(read_numbers('input\\day9.txt'))
    low_points, risk_levels = full_heightmap.find_low_points_and_risk_levels()
    print(f'Risk levels are {sum(risk_levels)}')
    basins = [full_heightmap.find_basin(y,x) for (y, x) in low_points]
    biggest_basin_sizes = [len(basin) for basin in basins]
    biggest_basin_sizes.sort(reverse=True)
    print(f'Three largest basins are {biggest_basin_sizes[0:3]}')