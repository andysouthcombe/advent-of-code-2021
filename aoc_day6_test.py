from os import read
import pytest

from aoc_day6 import day_pass, get_number_fish_per_age, pass_days, read_file

test_fishes = read_file('input\\day6_test.txt')
fish_per_age = get_number_fish_per_age(test_fishes)

def test_file_read_ok():
    assert len(test_fishes) == 5

def test_fish_per_age_totals_test_input():
    assert len(fish_per_age) == 9
    assert fish_per_age == [0,1,1,2,1,0,0,0,0]

def test_timer_decrements_number_greater_than_1():
    assert day_pass(test_fishes)[0] == 2

def test_timer_decrements_0_to_6():
    day_1 = day_pass(test_fishes)
    day_2 = day_pass(day_1)
    assert day_2[3] == 6

def test_extra_fish_when_hit_zero():
    day_1 = day_pass(test_fishes)
    day_2 = day_pass(day_1)
    assert len(day_2) == len(test_fishes)+1
    assert day_2[-1] == 8

def test_pass_days_gives_right_number_of_fish_for_test_case():
    output_fish = pass_days(test_fishes, 18)
    print(output_fish)
    assert len(output_fish) == 26