def read_file(filename):
    with open(filename,'r') as f:
        return f.read().splitlines()

def read_numbers(filename):
    raw_numbers = read_file(filename)
    return raw_numbers[0].split(',')