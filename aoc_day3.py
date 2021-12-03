from collections import Counter

def get_column_counts(input_list, column_num):
    column_vals = [row[column_num] for row in input_list]
    return Counter(column_vals)

def most_common_bit(input_list, column_num):
    counts = get_column_counts(input_list, column_num)
    return counts.most_common()[0][0]

def read_input(filename):
    with open(filename,'r') as f:
        return f.readlines()
