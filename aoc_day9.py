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

def read_numbers(filename):
    with open(filename,'r') as f:
        return [line.rstrip() for line in f.readlines()]

