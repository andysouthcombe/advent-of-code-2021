with open('input\day1.txt','r') as f:
    depths = [int(depth) for depth in f]
depths_greater_than_previous = 0
windowed_depths_greater_than_previous = 0

for count, depth in enumerate(depths):
    if count > 0 and depth > depths[count - 1]:
        depths_greater_than_previous += 1

print("Single depths greater than previous %s " % depths_greater_than_previous)

for count, depth in enumerate(depths):
    if count > 2:
        depths_this_window = sum(depths[count-2:count+1])
        depths_prev_window = sum(depths[count-3:count])
        if depths_this_window > depths_prev_window:
            windowed_depths_greater_than_previous+=1

print("Windowed depths greater than previous %s" % windowed_depths_greater_than_previous)
