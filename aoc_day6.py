from os import read


def read_file(filename):
    with open(filename,'r') as f:
        line = f.read().rstrip()
        return [int(num) for num in line.split(',')]

def get_number_fish_per_age(fishes):
    fish_per_age=[]
    for age in range(0, 9):
        fish_per_age.append(fishes.count(age))
    return fish_per_age

def day_pass(starting_fish_per_age):
    fish_per_age_day_later = []
    for index in range(0,len(starting_fish_per_age)-1):
        fish_per_age_day_later.append(starting_fish_per_age[index+1])
    fish_per_age_day_later[6] = fish_per_age_day_later[6] + starting_fish_per_age[0]
    fish_per_age_day_later.append(starting_fish_per_age[0])
    return fish_per_age_day_later

def pass_days(starting_fish_per_age,number_of_days):
    output_fish_per_age = starting_fish_per_age
    day = 1
    while day <= number_of_days:
        output_fish_per_age = day_pass(output_fish_per_age)
        day += 1
    return output_fish_per_age

if __name__ == '__main__':
    fishes = read_file('input\\day6.txt')
    fish_per_age = get_number_fish_per_age(fishes)
    resulting_fish = pass_days(fish_per_age, 80)
    print(f'After 80 days we have {sum(resulting_fish)} fish')
    resulting_fish = pass_days(fish_per_age, 256)
    print(f'After 256 days we have {sum(resulting_fish)} fish')