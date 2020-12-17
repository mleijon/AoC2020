from operator import add, mul

with open('p12_input.txt') as fi:
    data = [(x[0], int(x[1:].strip())) for x in fi.readlines()]


def rot(dir, turn):
    stp = turn[0]
    val = turn[1]
    ror = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
    rol = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    if stp == 'R':
        newdir = ror[(ror.index(dir) + val//45) % 8]
    else:
        newdir = rol[(rol.index(dir) + val//45) % 8]
    return newdir


def mvstp(mode, pos, dir):
    if mode == 'move_ship':
        coord = pos
    else:
        coord = dir
    for item in data:
        stp, val = item
        if stp == 'N':
            coord = list(map(add, coord, (0, val)))
        elif stp == 'S':
            coord = list(map(add, coord, (0, -val)))
        elif stp == 'W':
            coord = list(map(add, coord, (-val, 0)))
        elif stp == 'E':
            coord = list(map(add, coord, (val, 0)))
        elif stp == 'F':
            coord = list(map(add, coord, list(map(mul, (val, val), dir))))
        else:
            dir = rot(dir, item)
    return abs(coord[0]) + abs(coord[1])


print('The answer to part 1 is: {}'.format(mvstp('move_ship', (0, 0), (1, 0))))
