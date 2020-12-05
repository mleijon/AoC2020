with open('p5_input.txt') as fi:
    in_data = fi.read().split('\n')
    ID_max = 0
    planeIDs = set()
    for item in in_data:
        row_step = 64
        col_step = 4
        min_row = min_col = 0
        max_row = 127
        max_col = 7
        for char in item[:-3]:
            if char == 'F':
                max_row -= row_step
            else:
                min_row -= row_step
            row_step = row_step >> 1
        row = max_row
        for char in item[7:]:
            if char == 'R':
                min_col += col_step
            else:
                max_col -= col_step
            col_step = col_step >> 1
        col = max_col
        ID = 8*row + col
        planeIDs.add(ID)
        if ID > ID_max:
            ID_max = ID
    print('The answer to part 1 is: {}'.format(ID_max))
    allIDs = set()
    for row in range(127):
        for col in range(7):
            allIDs.add(8*row + col)
    missingIDs = allIDs - planeIDs
    for item in missingIDs:
        if (item + 1) not in missingIDs and (item - 1) not in missingIDs:
            print('The answer to part 2 is: {}'.format(item))
