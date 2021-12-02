from os import read


class SubmarinePart1:
    def __init__(self):
        self.depth = 0
        self.horizontal = 0
        self.mulitpliers = {'forward':1, 'up': -1, 'down':1}

    def move(self, directions):
        (direction, distance) = directions
        if direction == 'forward':
            self.horizontal += (distance * self.mulitpliers[direction])
        else:
            self.depth += (distance * self.mulitpliers[direction])

    def print_position(self):
        print(f'position is H: {self.horizontal}, D: {self.depth}')


class SubmarinePart2():
    def __init__(self,depth=0, horizontal=0, aim=0):
        self.depth = depth
        self.horizontal = horizontal
        self.aim = aim
        self.mulitpliers = {'forward':1, 'down':1, 'up':-1}

    def move(self, directions):
        (direction, distance) = directions
        if direction == 'forward':
            self.horizontal += (distance * self.mulitpliers[direction])
        else:
            self.aim += (distance * self.mulitpliers[direction])
    def print_position(self):
        print(f'position is H: {self.horizontal}, D: {self.depth}')

def read_input(filename):
    with open(filename,'r') as f:
        return [(direction, int(distance)) for direction, distance in [d.split() for d in f]]

def move_sub(sub:SubmarinePart1, filename:str)-> SubmarinePart1:
    directions = read_input(filename)
    moved_sub = sub
    for direction in directions:
        moved_sub.move(direction)
    return moved_sub

if __name__ == '__main__':
   sub = SubmarinePart1()
   moved_sub = move_sub(sub,'input\\day2.txt')
   moved_sub.print_position()
  