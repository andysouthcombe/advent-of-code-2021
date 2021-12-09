import pytest

from day_8 import count_digits_in_output_with_distinct_signal_count, decode_list_of_signals_and_sum_output, decode_signals_and_output, find_known_digits_in_output, find_number_nine, find_number_six, get_signals_for_number, get_signals_with_distinct_counts, identify_signals_for_easy_numbers, identify_top_line, read_and_split_file

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
    assert identify_signals_for_easy_numbers(['be', 'cfbegad', 'cgeb', 'edb']) == [(set('be'), 1),(set('cfbegad'), 8), (set('cgeb'), 4),(set('edb'),7)]

def test_identify_top_line():
    assert identify_top_line('be', 'edb') == set('d')

def test_find_known_digits_in_output():
    known_signals = [('cegd', 4), ('cgb', 7), ('gbdefca', 8), ('cg', 1)]
    digits = ['gbdfcae', 'bgc', 'cg', 'cgb']
    assert find_known_digits_in_output(known_signals, digits) == [8,7,1,7]

def test_find_number_six():
    signals = ['fbegcd', 'cbd', 'adcefb', 'dageb', 'afcb', 'bc', 'aefdc', 'ecdab', 'fgdeca', 'fcdbega']
    output = ['efabcd', 'cedba', 'gadfec', 'cb']
    easy_number_signals = identify_signals_for_easy_numbers(signals + output)
    assert set(find_number_six(easy_number_signals, signals + output)) == set('gadfec')

def test_find_number_nine():
    signals = ['fbegcd', 'cbd', 'adcefb', 'dageb', 'afcb', 'bc', 'aefdc', 'ecdab', 'fgdeca', 'fcdbega']
    output = ['efabcd', 'cedba', 'gadfec', 'cb']
    easy_number_signals = identify_signals_for_easy_numbers(signals + output)
    top_line_signal = identify_top_line(get_signals_for_number(easy_number_signals,1),get_signals_for_number(easy_number_signals,7))
    assert set(find_number_nine(easy_number_signals, signals + output,top_line_signal)) == set('efabcd')

def test_find_number_zero():
    signals = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
    output = ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']
    known_signals, known_output_digits = decode_signals_and_output(signals, output)
    assert get_signals_for_number(known_signals,0) == set('cagedb')

def test_find_number_five():
    signals = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
    output = ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']
    known_signals, known_output_digits = decode_signals_and_output(signals, output)
    assert get_signals_for_number(known_signals,5) == set('cdfbe')

def test_find_number_two():
    signals = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
    output = ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']
    known_signals, known_output_digits = decode_signals_and_output(signals, output)
    assert get_signals_for_number(known_signals,2) == set('gcdfa')

def test_find_number_three():
    signals = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
    output = ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']
    known_signals, known_output_digits = decode_signals_and_output(signals, output)
    assert get_signals_for_number(known_signals,2) == set('gcdfa')

def test_decode_signals_easy_numbers():
     known_signals, known_output_digits = decode_signals_and_output(['egadfb', 'cdbfeg', 'cegd', 'fecab', 'cgb', 'gbdefca', 'cg', 'fgcdab', 'egfdb', 'bfceg'],['gbdfcae', 'bgc', 'cg', 'cgb'])
     assert known_output_digits == [8, 7, 1, 7]

def test_decode_signals_easy_numbers_and_nine():
    known_signals, known_output_digits = decode_signals_and_output( ['edbfga', 'begcd', 'cbg',  'gc',  'gcadebf',  'fbgde', 'acbgfd', 'abcde', 'gfcbed', 'gfec'], ['fcgedb', 'cgb', 'dgebacf', 'gc'])
    assert known_output_digits == [9, 7, 8, 1]

def test_decode_list_of_signals_and_sum_output_works_for_test_data():
    assert decode_list_of_signals_and_sum_output(test_signals, test_outputs) == 61229