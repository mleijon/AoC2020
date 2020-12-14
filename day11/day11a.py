data = []
with open('p11_input.txt') as fi:
    for line in fi:
        data.append(list(line))


def check_surroundings(inp_data, x, y):
    xmax = len(inp_data[0])
    ymax = len(inp_data)
    xmin = ymin = 0
    surrounding = []
    i = 1
    if x + i in range(xmin, xmax) and y in range(ymin, ymax):
        surrounding.append(inp_data[y][x + i])
        if y + i in range(ymin, ymax):
            surrounding.append(inp_data[y + i][x + i])
        if y - i in range(ymin, ymax):
            surrounding.append(inp_data[y - i][x + i])
    if x - i in range(xmin, xmax) and y in range(ymin, ymax):
        surrounding.append((inp_data[y][x - i]))
        if y + i in range(ymin, ymax):
            surrounding.append(inp_data[y + i][x - i])
        if y - i in range(ymin, ymax):
            surrounding.append(inp_data[y - i][x - i])
    if y + i in range(ymin, ymax) and x in range(xmin, xmax):
        surrounding.append(inp_data[y + i][x])
    if y - i in range(ymin, ymax) and x in range(xmin, xmax):
        surrounding.append(inp_data[y - i][x])
    return surrounding.count('#')


def iterate(data):
    no_change = True
    new_data = []
    for row in range(len(data)):
        new_data.append([])
        for col in range(len(data[0])):
            if check_surroundings(data, col, row) >= 4 and data[row][col]\
                    == '#':
                new_data[row].append('L')
                no_change = False
            elif check_surroundings(data, col, row) == 0 and data[row][col]\
                    == 'L':
                new_data[row].append('#')
                no_change = False
            else:
                new_data[row].append(data[row][col])
    if no_change:
        count = 0
        for item in new_data:
            count += item.count('#')
        print('The answer to part 1 is: {}'.format(count))
        exit(0)
    else:
        iterate(new_data)


iterate(data)

