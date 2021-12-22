from aoc_utils import read_file_of_strings

def extract_points_and_folds(raw_data):
    split_line = raw_data.index('')
    points = [(int(x), int(y)) for x,y in  [line.split(',') for line in raw_data[0:split_line]]]
    folds = [(axis, int(line)) for axis, line in [fold.replace('fold along ','').split('=') for fold in raw_data[split_line+1:]]]
    return points, folds

def fold_on_axis(points, fold_axis, line_number):
    if fold_axis == 'x':
        return [(x - (line_number + 1), y) for x, y in points]
    else:
        return [(x, y - (line_number + 1)) for x, y in points]

if __name__ == '__main__':
    print(extract_points_and_folds(read_file_of_strings('input\\day13_test.txt')))