import pytest

from aoc_day3 import most_common_bit,read_input

def test_returns_correct_count_for_first_test_column():
    input_bits = read_input('input\\day3_test.txt')
    output = most_common_bit(input_bits,0)
    assert output == '1'

def test_returns_correct_count_for_second_test_column():
    input_bits = read_input('input\\day3_test.txt')
    output = most_common_bit(input_bits,1)
    assert output == '0'
