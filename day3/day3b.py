def race(hor_stp, vert_stp):
    with open('p3_input.txt') as fi:
        col = 0
        count = 0
        for i, line in enumerate(fi):
            if line[col % 31] == '#' and not i % vert_stp:
                count += 1
            col += hor_stp*(not i % vert_stp)
    return count


print(race(1, 1)*race(3, 1)*race(5, 1)*race(7, 1)*race(1, 2))
