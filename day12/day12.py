with open('p12_input.txt') as fi:
    data = [(x[0], int(x[1:].strip())) for x in fi.readlines()]


def rot(dir, turn):
    stp = turn[0]
    val = int(turn[1:])
    rotr = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    rotl = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    if stp == 'R':
        newdir = rotr[(rotr.index(dir) + val//90) % 4]
    else:
        newdir = rotl[(rotl.index(dir) + val//90) % 4]
    return newdir

# def mvstp(pos, dir):
#     for item in data:
#         stp, val = item
#
#         elif stp == 'N':
#             pass
#         elif stp == 'S':
#             pass
#         elif stp == 'W':
#             pass
#         elif stp == 'E':
#             pass
#         elif stp == 'F':
#             pass
#         else:
#             exit('wtf')


print(rot((1, 0), 'R90'))