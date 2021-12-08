from aoc_utils import read_one_line_int_file

def get_crab_sub_position_range(sub_positions):
    return min(sub_positions), max(sub_positions)

def get_move_cost(current_position,target_position):
    return abs(target_position - current_position)

def get_total_move_cost_to_position(sub_positions, target_position):
    return sum([get_move_cost(sub_position,target_position) for sub_position in sub_positions])