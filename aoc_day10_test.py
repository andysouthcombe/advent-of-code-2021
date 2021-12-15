import pytest

from aoc_day10 import get_invalid_closing_character, score_invalid_chars_part_1,finish_incomplete_string, score_missing_chars_part_2

test_input_valid_1 = '()'
test_input_valid_2 = '()()<>{()}'
test_input_invalid_1 = '(]'
test_input_invalid_2 = '{()()<>()>'
test_input_invalid_3 = '{([(<{}[<>[]}>{[]{[(<()>'
test_input_part_1 = [
                        '{([(<{}[<>[]}>{[]{[(<()>',
                        '[[<[([]))<([[{}[[()]]]',
                        '[{[{({}]{}}([{[{{{}}([]',
                        '[<(<(<(<{}))><([]([]()',
                        '<{([([[(<>()){}]>(<<{{'
                    ] 

test_input_part_2 = [
                        '[({(<(())[]>[[{[]{<()<>>',
                        '[(()[<>])]({[<{<<[]>>(',
                        '(((({<>}<{<{<>}{[]{[]{}',
                        '{<[[]]>}<{[{[{[]{()[[[]',
                        '<{([{{}}[<[[[<>{}]]]>[]]'
                    ]

def test_simple_valid_input_returns_none():
    assert get_invalid_closing_character(test_input_part_2[0]) == None

def test_incomplete_input_returns_none():
    assert get_invalid_closing_character(test_input_valid_1) == None

def test_simple_invalid_input_returns_square_bracket():
    assert get_invalid_closing_character(test_input_invalid_1) == ']'

def test_complex_valid_input_returns_none():
    assert get_invalid_closing_character(test_input_valid_2) == None

def test_complex_valid_input_returns_none():
    assert get_invalid_closing_character(test_input_invalid_2) == '>'

def test_very_complex_valid_input_returns_none():
    assert get_invalid_closing_character(test_input_invalid_3) == '}'

def test_score_invalid_chars_part_1_works_test_input():
    assert score_invalid_chars_part_1(test_input_part_1) == 26397

def test_finishes_first_incomplete_string():
    assert finish_incomplete_string(test_input_part_2[0]) == ['}', '}' ,']' ,']' ,')' ,'}' ,')' ,']']

def test_scores_test_incomplete_strings():
    assert score_missing_chars_part_2(test_input_part_2) == 288957
