import pytest

from aoc_day3 import get_co2_rating, get_epsilon_rate, get_gamma_rate, get_oxygen_rating, least_common_bit, most_common_bit, read_input

input_bits = read_input('input\\day3_test.txt')

def test_returns_correct_common_bit_for_first_test_column():
    output = most_common_bit(input_bits,0)
    assert output == '1'

def test_returns_correct_common_bit_for_second_test_column():
    output = most_common_bit(input_bits,1)
    assert output == '0'

def test_get_gamma_rate_works_for_sample():
    output = get_gamma_rate(input_bits)
    assert output == '10110'

def test_returns_correct_least_common_bit_for_first_test_column():
    output = least_common_bit(input_bits,0)
    assert output == '0'

def test_returns_correct_least_common_bit_for_second_test_column():
    output = least_common_bit(input_bits,1)
    assert output == '1'

def test_get_epsilon_rate_works_for_sample():
    output = get_epsilon_rate(input_bits)
    assert output == '01001'

def test_epsilon_times_gamma_is_correct():
    gamma_binary = get_gamma_rate(input_bits)
    epsilon_binary = get_epsilon_rate(input_bits)
    assert int(gamma_binary, 2) * int(epsilon_binary, 2) == 198

def test_get_oxygen_rating_correct_for_sample_data():
    assert get_oxygen_rating(input_bits) == 23

def test_get_co2_rating_correct_for_sample_data():
    assert get_co2_rating(input_bits) == 10
