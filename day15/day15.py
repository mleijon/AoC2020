turns = {16: (1, 1), 1: (2, 2), 0: (3, 3), 18: (4, 4), 12: (5, 5), 14: (6, 6)}
turn_nr = len(turns) + 1
current_key = 19
while turn_nr < 30000000:
    if current_key in turns.keys():
        turns[current_key] = (turn_nr, turns[current_key][0])
    else:
        turns.update({current_key: (turn_nr, turn_nr)})
    turn_nr += 1
    current_key = turns[current_key][0] - turns[current_key][1]
print('The answer to part 2 is: {}'.format(current_key))
