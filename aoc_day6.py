def read_file(filename):
    with open(filename,'r') as f:
        line = f.read().rstrip()
        return [int(num) for num in line.split(',')]

def decrement_timer(fish_timer):
    if fish_timer -1 < 0:
        return 6
    else:
        return fish_timer -1

def day_pass(fishes):
    return [decrement_timer(fish_timer) for fish_timer in fishes]