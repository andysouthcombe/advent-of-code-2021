f = open('input\day1.txt','r')
depths = f.readlines()
depths_greater_than_previous = 0

for count, depth in enumerate(depths):
    if count > 0 and int(depth) > int(depths[count - 1]):
        depths_greater_than_previous += 1

print(depths_greater_than_previous)




