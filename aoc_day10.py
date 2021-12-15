from os import close
from aoc_utils import read_file_of_strings

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

def get_invalid_closing_character(input):
    open_chars = []
    for char in input:
        if char in open_to_closing_chars:
            open_chars.append(char)
        if char in closing_to_open_chars:
            if open_chars[-1] == closing_to_open_chars[char]:
                open_chars.pop(-1)
            else:
                return char
    return None

def score_invalid_chars_part_1(inputs):
    invalid_chars = [get_invalid_closing_character(input) for input in inputs]
    return sum([invalid_closing_char_scores[invalid_char] for invalid_char in invalid_chars if invalid_char is not None])

if __name__ == '__main__':
    print(score_invalid_chars_part_1(read_file_of_strings('input\\day10.txt')))