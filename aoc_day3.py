from collections import Counter

def read_input(filename):
    with open(filename,'r') as f:
        return f.read().splitlines()

def get_column_counts(input_list, column_num):
    column_vals = [row[column_num] for row in input_list]
    return Counter(column_vals)

def most_common_bit(input_list, column_num):
    counts = get_column_counts(input_list, column_num)
    return counts.most_common()[0][0]

def least_common_bit(input_list, column_num):
    counts = get_column_counts(input_list, column_num)
    return counts.most_common()[-1][0]

def get_gamma_rate(input_list):
    num_cols = len(input_list[0])
    most_popular_bits = ''
    for c in range(num_cols):
        most_popular_bits += most_common_bit(input_list, c)
    return most_popular_bits

def get_epsilon_rate(input_list):
    num_cols = len(input_list[0])
    least_popular_bits = ''
    for c in range(num_cols):
        least_popular_bits += least_common_bit(input_list, c)
    return least_popular_bits
