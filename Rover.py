class Rover(object):
    RIGHT_TURN_MAP = {'E' : 'S', 'S': 'W', 'W': 'N', 'N': 'E'}
    LEFT_TURN_MAP = {'E' : 'N', 'S': 'E', 'W': 'S', 'N': 'W'}
    X_MOVE_MAP = {'E' : 1, 'S': 0, 'W': -1, 'N': 0}
    Y_MOVE_MAP = {'E' : 0, 'S': -1, 'W': 0, 'N': 1}

    def __init__(self, x, y, facing):
        self.__facing = facing
        self.__x = x
        self.__y = y

    def move(self, command):
        if command == 'R':
            self.__facing = self.RIGHT_TURN_MAP[self.__facing]
        elif command == 'L':
            self.__facing = self.LEFT_TURN_MAP[self.__facing]
        else:
            self.__x += self.X_MOVE_MAP[self.__facing]
            self.__y += self.Y_MOVE_MAP[self.__facing]

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def facing(self):
        return self.__facing

class Plateau(object):
    def __init__(self, right, top):
        self.__right = right
        self.__top = top
        self.__rovers = []

    @property
    def rovers(self):
        return self.__rovers

    def addRover(self, x, y, facing, moves):
        if not self.__valid_position(x, y):
            return None
        r = Rover(x, y, facing)
        for command in moves:
            if self.__valid(r, command):
                r.move(command)
        self.__rovers.append(r)
        return r

    def __valid(self, r, command):
        if command == 'M':
            new_x = r.x + Rover.X_MOVE_MAP[r.facing]
            new_y = r.y + Rover.Y_MOVE_MAP[r.facing]
            return self.__valid_position(new_x, new_y)
        return command in 'RL'

    def __valid_position(self, x, y):
        if x < 0 or y < 0 or x > self.__right or y > self.__top:
            return False
        # dont't allow running into an existing rover
        for rover in self.__rovers:
            if rover.x == x and rover.y == y:
                return False
        return True


if __name__ == '__main__':
    import sys
    infile = sys.stdin
    plateau_size = infile.readline().rstrip().split(' ')
    plateau = Plateau(int(plateau_size[0]), int(plateau_size[1]))

    while True:
        roverline = infile.readline()
        if not roverline:
            break
        rover = roverline.rstrip().split(' ')
        moves = infile.readline().rstrip()
        plateau.addRover(int(rover[0]), int(rover[1]), rover[2], moves)

    for rover in plateau.rovers:
        print(rover.x, rover.y, rover.facing)
