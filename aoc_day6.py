def read_file(filename):
    with open(filename,'r') as f:
        line = f.read().rstrip()
        return [int(num) for num in line.split(',')]

def get_number_fish_per_age(fishes):
    fish_per_age=[]
    for age in range(0, 9):
        fish_per_age.append(fishes.count(age))
    return fish_per_age

def day_pass(fish_per_age):
    fish_day_later = []
    for index in range(0,len(fish_per_age)):
        if index < 8:
            fish_day_later.append(fish_per_age[index+1])
    return fish_day_later

        

# def pass_days(fishes,number_of_days):
#     output_fishes = fishes
#     day = 1
#     while day <= number_of_days:
#         output_fishes = day_pass(output_fishes)
#         day += 1
#     return output_fishes

# if __name__ == '__main__':
    # fishes = read_file('input\\day6.txt')
    # resulting_fish = pass_days(fishes, 80)
    # print(f'After 80 days we have {len(resulting_fish)} fish')
    # #resulting_fish = pass_days(fishes, 256)
    # print(f'After 256 days we have {len(resulting_fish)} fish')