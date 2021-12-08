from aoc_utils import read_one_line_int_file

def get_crab_sub_position_range(sub_positions):
    return min(sub_positions), max(sub_positions)

def get_move_cost(current_position,target_position):
    return abs(target_position - current_position)
