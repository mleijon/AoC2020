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
            if mode == 'move_ship':
                coord = list(map(add, coord, (0, val)))
            else:
                pass
        elif stp == 'S':
            if mode == 'move_ship':
                coord = list(map(add, coord, (0, -val)))
            else:
                pass
        elif stp == 'W':
            if mode == 'move_ship':
                coord = list(map(add, coord, (-val, 0)))
            else:
                pass
        elif stp == 'E':
            if mode == 'move_ship':
                coord = list(map(add, coord, (val, 0)))
            else:
                pass
        elif stp == 'F':
            if mode == 'move_ship':
                coord = list(map(add, coord, list(map(mul, (val, val), dir))))
            else:
                pass
        else:
            if 0 in dir:
            #     dir = rot(dir, item)
            # else:
                dir_0m = abs(dir[0])
                dir_0 = (int(dir[0]/dir_0m), 0)
                dir_0 = rot(dir_0, item)
                dir_0 = tuple(map(mul, (dir_0m, dir_0m), dir_0))
                dir_1m = abs(dir[1])
                dir_1 = (0, int(dir[1]/dir_1m))
                dir_1 = rot(dir_1, item)
                dir_1 = tuple(map(mul, (dir_1m, dir_1m), dir_1))
                dir = tuple(map(add, dir_0, dir_1))

    return abs(coord[0]) + abs(coord[1])


print('The answer to part 1 is: {}'.format(mvstp('move_ship', (0, 0), (1, 0))))
