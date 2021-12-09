def read_numbers(filename):
    with open(filename,'r') as f:
        return [line.rstrip() for line in f.readlines()]

def get_neighbour_square_values(test_numbers, x, y):
    above = test_numbers[y-1][x]
    right = test_numbers[y][x+1]
    left = test_numbers[y][x-1]
    below = test_numbers[y+1][x]
    return [above, right,below,left]