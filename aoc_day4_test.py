import pytest

from aoc_day4 import read_cards, read_numbers, Card

numbers = read_numbers('input\\day_4_test_numbers.txt')
cards = read_cards('input\\day_4_test_cards.txt')

def test_numbers_read_in_ok():
    assert numbers[0] == 7
    assert len(numbers) == 27

def test_card_rows_read_in_ok():
    assert cards[0].rows[0] == [22,13,17,11,0]
    assert cards[2].rows[4] == [2,0,12,3,7]

def test_card_columns_read_in_ok():
    assert cards[0].columns[0] == [22,8,21,6,1]
    assert cards[2].columns[4] == [4,19,20,5,7]

def test_mark_single_number():
    card = cards[1]
    assert card.mark_number(8, card.rows[2]) == [19,7,25,23]

