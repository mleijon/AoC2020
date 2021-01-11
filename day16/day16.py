allowed_numbers = set()
tser = 0
with open('p16_input.txt') as fi:
    for row in fi.readlines():
        if 'or' in row:
            rl = row.split(' ')[-3].split('-')
            rh = row.split(' ')[-1].strip().split('-')
            allowed_numbers.update(set(range(int(rl[0]), int(rl[1]) + 1)))
            allowed_numbers.update(set(range(int(rh[0]), int(rh[1]) + 1)))
        elif ',' in row:
            for item in row.strip().split(','):
                if int(item) not in allowed_numbers:
                    tser += int(item)
print('The answer to part 1 is: {}'.format(tser))

