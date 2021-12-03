from collections import Counter
from os import read

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

def get_oxygen_rating(input_list):
    num_cols = len(input_list[0])
    output_list = input_list
    for c in range(num_cols):
        num_rows = len(output_list)
        counts = get_column_counts(output_list, c)
        sorted_counts = counts.most_common()
        if sorted_counts[0][1] == sorted_counts[1][1]:
            #tie so for oxygen set most common = 1
            most_common = '1'
        else:
            most_common = sorted_counts[0][0]
        new_output_list = []
        
        for r in range(num_rows) :    
            if output_list[r][c] == most_common:
                new_output_list.append(output_list[r])
        output_list = new_output_list
        if len(output_list) == 1:
            break
    return int(output_list[0],2)

def get_co2_rating(input_list):
    num_cols = len(input_list[0])
    output_list = input_list
    for c in range(num_cols):
        num_rows = len(output_list)
        counts = get_column_counts(output_list, c)
        sorted_counts = counts.most_common()
        if sorted_counts[0][1] == sorted_counts[1][1]:
            #tie so for CO2 set most common = 0
            least_common = '0'
        else:
            least_common = sorted_counts[1][0]
        new_output_list = []
        
        for r in range(num_rows) :    
            if output_list[r][c] == least_common:
                new_output_list.append(output_list[r])
        output_list = new_output_list
        if len(output_list) == 1:
            break
    return int(output_list[0],2)



if __name__ == '__main__':
    input_bits = read_input('input\\day3.txt')
    epsilon_binary = get_epsilon_rate(input_bits)
    gamma_binary = get_gamma_rate(input_bits)
    power_consumption = int(gamma_binary, 2) * int(epsilon_binary, 2)
    print(f'Gamma_Binary is {gamma_binary} Epsilon_Binary is {epsilon_binary} Power Consumption is {power_consumption}')

    