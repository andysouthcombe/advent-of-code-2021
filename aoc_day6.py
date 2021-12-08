def read_file(filename):
    with open(filename,'r') as f:
        line = f.read().rstrip()
        return [int(num) for num in line.split(',')]

def day_pass(fishes):
    return [fish_timer - 1 for fish_timer in fishes]