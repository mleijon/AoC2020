import copy
operations = dict()
op_nr = 0
with open('p8_input.txt') as fi:
    for i, line in enumerate(fi.readlines()):
        operations[i] = [line.split(' ')[0], int(line.split(' ')[1].strip()),
                         False]
max_op_nr = len(operations)
new_operations = copy.deepcopy(operations)


def run_code(ops):
    global max_op_nr
    global op_nr
    accumulator = 0
    while True:
        if op_nr == max_op_nr:
            return accumulator
        elif ops[op_nr][2]:
            return accumulator
        else:
            ops[op_nr][2] = True
            if ops[op_nr][0] == 'acc':
                accumulator += ops[op_nr][1]
                op_nr += 1
            elif ops[op_nr][0] == 'nop':
                op_nr += 1
            else:
                op_nr += ops[op_nr][1]


print('The answer to part 1 is: {}'.format(run_code(new_operations)))
for key in operations.keys():
    op_nr = 0
    new_operations = copy.deepcopy(operations)
    if operations[key][0] == 'nop':
        new_operations[key][0] = 'jmp'
    elif operations[key][0] == 'jmp':
        new_operations[key][0] = 'nop'
    acc = run_code(new_operations)
    if op_nr == max_op_nr:
        print('The answer to part 2 is: {}'.format(acc))
        exit(0)
