from aoc_utils import read_file_of_strings

def extract_points_and_folds(raw_data):
    split_line = raw_data.index('')
    points = [(int(x), int(y)) for x,y in  [line.split(',') for line in raw_data[0:split_line]]]
    folds = [(axis, int(line)) for axis, line in [fold.replace('fold along ','').split('=') for fold in raw_data[split_line+1:]]]
    return points, folds

def fold_on_axis(points, fold_axis, line_number):
    if fold_axis == 'x':
        return list(set([(line_number - (x - line_number), y) for x, y in points if x > line_number] + [(x, y) for x, y in points if x < line_number]))
    else:
        return list(set([(x, line_number - (y- line_number)) for x, y in points if y > line_number] + [(x, y) for x, y in points if y < line_number]))

def print_points(points):
    max_x = max([point[0] for point in points])
    max_y = max([point[1] for point in points])
    for y in range (0, max_y + 1):
        for x in range (0, max_x + 1):
            if (x, y) in points:
                print('#',end='')
            else:
                print('.',end='')
        print('', end='\n')



if __name__ == '__main__':
    points, folds = extract_points_and_folds(read_file_of_strings('input\\day13.txt'))
    axis, line = folds[0]
    print(len(fold_on_axis(points, axis, line)))
    for axis, line in folds:
        points = fold_on_axis(points, axis, line)
    print_points(points)
    print(len(points))