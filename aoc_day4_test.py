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
    assert cards[0].get_columns()[0] == [22,8,21,6,1]
    assert cards[2].get_columns()[4] == [4,19,20,5,7]


def test_not_won_yet():
     card = cards[0]
     we_have_a_winner = False
     test_numbers = [18, 23]
     we_have_a_winner = card.check_for_winner(test_numbers)
     assert we_have_a_winner == False

def test_winner():
     card = cards[0]
     we_have_a_winner = False
     test_numbers = [18, 5, 3, 10, 6]
     we_have_a_winner = card.check_for_winner(test_numbers)
     assert we_have_a_winner == True

def test_sum_remaining():
    card = cards[0]
    test_numbers = [18, 5, 3, 10, 6]
    print(card.sum_remaining_numbers(test_numbers))
    assert card.check_for_winner(test_numbers) == True
    assert card.sum_remaining_numbers(test_numbers) == 258