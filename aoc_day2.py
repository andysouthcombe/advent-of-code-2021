class Submarine:
    def __init__(self):
        self.depth = 0
        self.horizontal = 0
        self.mulitpliers = {'foward':1, 'up': -1, 'down':1}

    def move(self, direction,distance):
        if direction == 'forward':
            self.horizontal += (distance * self.mulitpliers['direction'])
        else:
            self.depth += (distance * self.mulitpliers['direction'])
        return f'new position is H: {self.horizontal}, D: {self.depth}'

def read_input(filename):
    with open(filename,'r') as f:
        return [(direction, int(distance)) for direction, distance in [d.split() for d in f]]

if __name__ == '__main__':
   print('hello')
