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

def test_card_marked_correctly():
    card = cards[0]
    for number in [18, 23]:
        card.mark_card_and_see_if_winner(number)
    assert card.rows[3] == [6, 10, 3, 5]
    assert card.rows[1] == [8, 2, 4, 24]
    assert card.columns[3] == [11, 4, 16, 15]
    assert card.columns[2] == [17, 14, 3, 20]

def test_not_won_yet():
    card = cards[0]
    we_have_a_winner = False
    for number in [18, 23]:
        we_have_a_winner = card.mark_card_and_see_if_winner(number)
    assert we_have_a_winner == False

def test_winner():
    card = cards[0]
    we_have_a_winner = False
    for number in [18, 5, 3, 10, 6]:
        we_have_a_winner = card.mark_card_and_see_if_winner(number)
    print(card.rows)
    print(card.check_for_winner(card.rows[3]))
    assert we_have_a_winner == True