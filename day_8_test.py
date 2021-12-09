import pytest

from day_8 import count_digits_in_output_with_distinct_signal_count, decode_signals_and_output, find_known_digits_in_output, find_number_six, get_signals_with_distinct_counts, identify_signals_for_easy_numbers, identify_top_line, read_and_split_file

test_signals, test_outputs = read_and_split_file('input\\day8_test.txt')

def test_file_read_ok():
    assert test_signals[0][2] == 'cbdgef'
    assert test_signals[1][3] == 'gc'
    assert test_outputs[2][3] == 'cbg'

def test_count_distinct_digits_in_test_output():
    assert count_digits_in_output_with_distinct_signal_count(test_outputs) == 26

def test_get_signals_with_distinct_counts_returns_right_signals():
    assert get_signals_with_distinct_counts(test_signals[0])== ['be', 'cfbegad', 'cgeb', 'edb']

def test_identify_signals_for_easy_numbers():
    assert identify_signals_for_easy_numbers(['be', 'cfbegad', 'cgeb', 'edb']) == [('be', 1),('cfbegad', 8), ('cgeb', 4),('edb',7)]

def test_identify_top_line():
    assert identify_top_line('be', 'edb') == 'd'

def test_find_known_digits_in_output():
    known_signals = [('cegd', 4), ('cgb', 7), ('gbdefca', 8), ('cg', 1)]
    digits = ['gbdfcae', 'bgc', 'cg', 'cgb']
    assert find_known_digits_in_output(known_signals, digits) == [8,7,1,7]

def test_find_number_six():
    signals = ['fbegcd', 'cbd', 'adcefb', 'dageb', 'afcb', 'bc', 'aefdc', 'ecdab', 'fgdeca', 'fcdbega']
    output = ['efabcd', 'cedba', 'gadfec', 'cb']
    easy_number_signals = identify_signals_for_easy_numbers(signals + output)
    assert set(find_number_six(easy_number_signals, signals + output)) == set('gadfec')


def test_decode_signals_easy_numbers():
    assert decode_signals_and_output(['egadfb', 'cdbfeg', 'cegd', 'fecab', 'cgb', 'gbdefca', 'cg', 'fgcdab', 'egfdb', 'bfceg'],['gbdfcae', 'bgc', 'cg', 'cgb']) == [8, 7, 1, 7]