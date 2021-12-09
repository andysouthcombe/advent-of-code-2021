def read_numbers(filename):
    with open(filename,'r') as f:
        return [line.rstrip() for line in f.readlines()]
        