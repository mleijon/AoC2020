operations = dict()
accumulator = op_nr = 0
with open('p8_input.txt') as fi:
    for i, line in enumerate(fi.readlines()):
        operations[i] = [line.split(' ')[0], int(line.split(' ')[1].strip()),
                         False]
while True:
    if operations[op_nr][2]:
        print('The answer to part 1 is: {}'.format(accumulator))
        break
    else:
        operations[op_nr][2] = True
        if operations[op_nr][0] == 'acc':
            accumulator += operations[op_nr][1]
            op_nr += 1
        elif operations[op_nr][0] == 'nop':
            op_nr += 1
        else:
            op_nr += operations[op_nr][1]
