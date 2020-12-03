with open('p3_input.txt')  as fi:
    col = 0
    count = 0
    for line in fi:
        if line[col % 31] == '#':
            count += 1
        col += 3
print(count)