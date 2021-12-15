from os import close
from aoc_utils import read_file_of_strings
from statistics import median

open_to_closing_chars = {
                            '(': ')',
                            '<': '>',
                            '[': ']',
                            '{': '}'
                        }

closing_to_open_chars = {value:key for key, value in open_to_closing_chars.items()}

invalid_closing_char_scores = {
                                ')': 3,
                                ']': 57,
                                '}': 1197,
                                '>': 25137
                                }

missing_char_scores =   {
                                ')': 1,
                                ']': 2,
                                '}': 3,
                                '>': 4
                        }

def get_invalid_closing_character(input):
    open_chars = []
    for char in input:
        if char in open_to_closing_chars:
            open_chars.append(char)
        if char in closing_to_open_chars:
            if open_chars[-1] == closing_to_open_chars[char]:
                open_chars.pop()
            else:
                return char
    return None

def finish_incomplete_string(input):
    opening_chars = []
    for char in input:
        if char in open_to_closing_chars:
            opening_chars.append(char)
        if char in closing_to_open_chars:
            opening_chars.pop()
    opening_chars.reverse()
    return [open_to_closing_chars[char] for char in opening_chars]

def score_invalid_chars_part_1(inputs):
    invalid_chars = [get_invalid_closing_character(input) for input in inputs]
    return sum([invalid_closing_char_scores[invalid_char] for invalid_char in invalid_chars if invalid_char is not None])

def score_missing_chars_part_2(inputs):
    incomplete_lines = [input for input in inputs if get_invalid_closing_character(input) is None]
    missing_chars = [finish_incomplete_string(line) for line in incomplete_lines]
    scores = []
    for missing_char_line in missing_chars:
        score = 0
        for missing_char in missing_char_line:
            score = (score * 5) + missing_char_scores[missing_char]
        scores.append(score)
    return median(scores)


if __name__ == '__main__':
    print(score_invalid_chars_part_1(read_file_of_strings('input\\day10.txt')))
    print(score_missing_chars_part_2(read_file_of_strings('input\\day10.txt')))