import time
start_time = time.time()
with open('input\day1.txt','r') as f:
    depths = [int(depth) for depth in f]
depths_greater_than_previous = 0
windowed_depths_greater_than_previous = 0

part1_start_time = time.time()
for count, depth in enumerate(depths):
    if count > 0 and depth > depths[count - 1]:
        depths_greater_than_previous += 1

part1_end_time = time.time()

part2_start_time = time.time()
for count, depth in enumerate(depths):
    if count > 2:
        depths_this_window = sum(depths[count-2:count+1])
        depths_prev_window = sum(depths[count-3:count])
        if depths_this_window > depths_prev_window:
            windowed_depths_greater_than_previous+=1
part2_end_time = time.time()

end_time = time.time()
print("Single depths greater than previous %s " % depths_greater_than_previous)
print("Windowed depths greater than previous %s" % windowed_depths_greater_than_previous)
print(f'Part1 Run time is {part1_end_time - part1_start_time}')
print(f'Part2 Run time is {part2_end_time - part2_start_time}')
print(f'Total Run time is {end_time - start_time}')
