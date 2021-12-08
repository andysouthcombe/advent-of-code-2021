from aoc_utils import read_one_line_int_file

def get_crab_sub_position_range(sub_positions):
    return min(sub_positions), max(sub_positions)

def get_move_cost(current_position,target_position):
    return abs(target_position - current_position)

def get_move_cost_part_2(current_position,target_position):
    distance = abs(target_position - current_position)
    return sum([step for step in range(0, distance+1)])


def get_total_move_cost_to_position(sub_positions, target_position,get_move_cost_part_1_or_2):
    return sum([get_move_cost_part_1_or_2(sub_position,target_position) for sub_position in sub_positions])

def get_cheapest_common_position(sub_positions, get_move_cost_part_1_or_2):
    min_position, max_position = get_crab_sub_position_range(sub_positions)
    return min([(target_position, get_total_move_cost_to_position(sub_positions,target_position,get_move_cost_part_1_or_2)) for target_position in range(min_position, max_position + 1)], key = lambda cost:cost[1])
    
if __name__ == '__main__':
    sub_positions = read_one_line_int_file('input\\day7.txt')
    print(f'cheapest position to move to for part 1 is {get_cheapest_common_position(sub_positions, get_move_cost)}')
    print(f'cheapest position to move to for part 2 is {get_cheapest_common_position(sub_positions, get_move_cost_part_2)}')