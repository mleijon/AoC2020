from operator import add, mul

with open('p12_input.txt') as fi:
    data = [(x[0], int(x[1:].strip())) for x in fi.readlines()]


def rot(dir, turn):
    stp = turn[0]
    val = turn[1]
    ror = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
    rol = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    if stp == 'R':
        return ror[(ror.index(dir) + val//45) % 8]
    else:
        return rol[(rol.index(dir) + val//45) % 8]


def mvstp(mode, pos, dir):
    for item in data:
        stp, val = item
        if stp == 'N':
            if mode == 'move_ship':
                pos = list(map(add, pos, (0, val)))
            else:
                dir = list(map(add, dir, (0, val)))
        elif stp == 'S':
            if mode == 'move_ship':
                pos = list(map(add, pos, (0, -val)))
            else:
                dir = list(map(add, dir, (0, -val)))
        elif stp == 'W':
            if mode == 'move_ship':
                pos = list(map(add, pos, (-val, 0)))
            else:
                dir = list(map(add, dir, (-val, 0)))
        elif stp == 'E':
            if mode == 'move_ship':
                pos = list(map(add, pos, (val, 0)))
            else:
                dir = list(map(add, dir, (val, 0)))
        elif stp == 'F':
            pos = list(map(add, pos, list(map(mul, (val, val), dir))))
        else:
            if 0 in dir:
                amp = max(abs(dir[0]), abs(dir[1]))
                dir = (int(dir[0]/amp), int(dir[1]/amp))
                dir = rot(dir, item)
                dir = tuple(map(mul, (amp, amp), dir))

            else:
                dir_0 = (int(dir[0]/abs(dir[0])), 0)
                dir_0 = rot(dir_0, item)
                dir_0 = tuple(map(mul, (abs(dir[0]), abs(dir[0])), dir_0))
                dir_1 = (0, int(dir[1]/abs(dir[1])))
                dir_1 = rot(dir_1, item)
                dir_1 = tuple(map(mul, (abs(dir[1]), abs(dir[1])), dir_1))
                dir = tuple(map(add, dir_0, dir_1))
    return abs(pos[0]) + abs(pos[1])


print('The answer to part 1 is: {}'.format(mvstp('move_ship', (0, 0), (1, 0))))
print('The answer to part 2 is: {}'.format(mvstp('move_wp', (0, 0), (10, 1))))
