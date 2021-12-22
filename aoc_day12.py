from aoc_utils import read_file_of_strings
from functools import lru_cache

def parse_route_list(filename):
    raw_list = [route.split('-') for route in read_file_of_strings(filename)]
    return [(start, end) for start, end in raw_list] + [(end, start) for start, end in raw_list ]
    
def get_routes_from_cave(cave, route_list):
    return [route[1] for route in route_list if cave == route[0]]

def is_cave_small(cave):
    return cave.islower()

def count_paths(cave_map, small_caves_twice):
    # Use functools.cache to eliminate unnecessary recursive calls.
    @lru_cache(maxsize=None)
    def count_next_paths(origin, seen, twice):
        if is_cave_small(origin):
            seen = seen.union({origin})
        n_paths = 0
        for target in get_routes_from_cave(origin, cave_map):
            if target == "end":
                n_paths += 1
            elif target not in seen:
                n_paths += count_next_paths(target, seen, twice)
            elif target != "start" and twice:
                n_paths += count_next_paths(target, seen, False)
        return n_paths
    return count_next_paths("start", frozenset(), small_caves_twice)

if __name__ == '__main__':
    routes = parse_route_list('input\\day12.txt')
    print(count_paths(routes,False))
    print(count_paths(routes,True))

