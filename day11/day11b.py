class Directions:
    n = s = e = w = nw = ne = sw = se = False

    def reset(self, bv):
        self.n = self.s = self.e = self.w = self.nw = self.ne = self.sw =\
            self.se = bv


data = []
with open('p11_input.txt') as fi:
    for line in fi:
        data.append(list(line))


def check_surroundings(inp_data, x, y):
    dirs = Directions()
    dirs.reset(False)
    xmax = len(inp_data[0])
    ymax = len(inp_data)
    xmin = ymin = 0
    surrounding = []
    i = 0
    while x - i in range(xmin, xmax) or x + i in range(xmin, xmax) or\
            y - i in range(ymin, ymax) or y + i in range(ymin, ymax):
        i += 1
        if x + i in range(xmin, xmax) and y in range(ymin, ymax):
            if dirs.e or inp_data[y][x + i] == '.':
                pass
            else:
                surrounding.append(inp_data[y][x + i])
                dirs.e = True
            if y + i in range(ymin, ymax):
                if dirs.se or inp_data[y + i][x + i] == '.':
                    pass
                else:
                    surrounding.append(inp_data[y + i][x + i])
                    dirs.se = True
            if y - i in range(ymin, ymax):
                if dirs.ne or inp_data[y - i][x + i] == '.':
                    pass
                else:
                    surrounding.append(inp_data[y - i][x + i])
                    dirs.ne = True
        if x - i in range(xmin, xmax) and y in range(ymin, ymax):
            if dirs.w or inp_data[y][x - i] == '.':
                pass
            else:
                surrounding.append((inp_data[y][x - i]))
                dirs.w = True
            if y + i in range(ymin, ymax):
                if dirs.sw or inp_data[y + i][x - i] == '.':
                    pass
                else:
                    surrounding.append(inp_data[y + i][x - i])
                    dirs.sw = True
            if y - i in range(ymin, ymax):
                if dirs.nw or inp_data[y - i][x - i] == '.':
                    pass
                else:
                    surrounding.append(inp_data[y - i][x - i])
                    dirs.nw = True
        if y + i in range(ymin, ymax) and x in range(xmin, xmax):
            if dirs.s or inp_data[y + i][x] == '.':
                pass
            else:
                surrounding.append(inp_data[y + i][x])
                dirs.s = True
        if y - i in range(ymin, ymax) and x in range(xmin, xmax):
            if dirs.n or inp_data[y - i][x] == '.':
                pass
            else:
                surrounding.append(inp_data[y - i][x])
                dirs.n = True
        if all([dirs.n, dirs.s, dirs.w, dirs.e, dirs.sw, dirs.se, dirs.ne,
                dirs.nw]):
            return surrounding.count('#')
    return surrounding.count('#')


def iterate(data):
    no_change = True
    new_data = []
    for row in range(len(data)):
        new_data.append([])
        for col in range(len(data[0])):
            if check_surroundings(data, col, row) >= 5 and data[row][col]\
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
        print('The answer to part 2 is: {}'.format(count))
        exit(0)
    else:
        iterate(new_data)


iterate(data)
