import pytest

from aoc_day3 import get_epsilon_rate, get_gamma_rate, least_common_bit, most_common_bit, read_input

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