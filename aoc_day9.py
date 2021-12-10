class heightmap:
    def __init__(self,squares):
        self.squares = squares
        self.max_y = len(squares) - 1
        self.max_x = len(squares[0]) - 1
    
    def get_neighbour_square_values(self, y, x):
        neighbours = []
        if self.has_above(y):
            neighbours.append(self.squares[y-1][x])
        neighbours.append(self.squares[y][x+1])
        neighbours.append(self.squares[y+1][x])
        neighbours.append(self.squares[y][x-1])
        return neighbours
    
    def has_above(self, y):
        return y > 0

        

def read_numbers(filename):
    with open(filename,'r') as f:
        return [line.rstrip() for line in f.readlines()]

