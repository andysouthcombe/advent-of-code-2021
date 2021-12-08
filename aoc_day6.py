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
    fish_about_to_breed = [fish_timer for fish_timer in fishes if fish_timer == 0]
    decremented_timers =[decrement_timer(fish_timer) for fish_timer in fishes]
    return decremented_timers + [8 for fish in fish_about_to_breed]

def pass_days(fishes,number_of_days):
    output_fishes = fishes
    day = 1
    while day <= number_of_days:
        output_fishes = day_pass(output_fishes)
        day += 1
    return output_fishes