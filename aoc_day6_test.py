from os import read
import pytest

from aoc_day6 import day_pass, get_number_fish_per_age, read_file

test_fishes = read_file('input\\day6_test.txt')
fish_per_age = get_number_fish_per_age(test_fishes)

def test_file_read_ok():
    assert len(test_fishes) == 5

def test_fish_per_age_totals_test_input():
    assert len(fish_per_age) == 9
    assert fish_per_age == [0,1,1,2,1,0,0,0,0]

def test_day_pass_moves_fish_ages_down():
    assert day_pass(fish_per_age)[0] == 1

def test_day_pass_resets_age_to_6():
    day_1 =  day_pass(fish_per_age)
    day_2 =  day_pass(day_1)
    assert day_2[6] == 1

def test_extra_fish_when_hit_zero():
     day_1 = day_pass(fish_per_age)
     day_2 = day_pass(day_1)
     assert day_2[8] == 1

# def test_pass_days_gives_right_number_of_fish_for_test_case():
#     output_fish = pass_days(test_fishes, 18)
#     print(output_fish)
#     assert len(output_fish) == 26