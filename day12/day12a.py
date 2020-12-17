from operator import add, mul

with open('p12_input.txt') as fi:
    data = [(x[0], int(x[1:].strip())) for x in fi.readlines()]


def rot(dir, turn):
    stp = turn[0]
    val = turn[1]
    rotr = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    rotl = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    if stp == 'R':
        newdir = rotr[(rotr.index(dir) + val//90) % 4]
    else:
        newdir = rotl[(rotl.index(dir) + val//90) % 4]
    return newdir


def mvstp(pos, dir):
    for item in data:
        stp, val = item
        if stp == 'N':
            pos = list(map(add, pos, (0, val)))
        elif stp == 'S':
            pos = list(map(add, pos, (0, -val)))
        elif stp == 'W':
            pos = list(map(add, pos, (-val, 0)))
        elif stp == 'E':
            pos = list(map(add, pos, (val, 0)))
        elif stp == 'F':
            pos = list(map(add, pos, list(map(mul, (val, val), dir))))
        else:
            dir = rot(dir, item)
    return abs(pos[0]) + abs(pos[1])


print('The answer to part 1 is: {}'.format(mvstp((0, 0), (1, 0))))
