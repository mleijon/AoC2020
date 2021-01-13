allowed_numbers = set()
cat_allowed_numbers = dict()
invalid_pass = set()
valid_pass = set()
all_pass = set()
cats = list()
tser = 0
multdep = 1
with open('p16_input.txt') as fi:
    for row in fi.readlines():
        if 'or' in row:
            cats.append([])
            rl = row.split(' ')[-3].split('-')
            rh = row.split(' ')[-1].strip().split('-')
            allowed_numbers.update(range(int(rl[0]), int(rl[1]) + 1))
            cat_allowed_numbers[row.split(':')[0]] = set(range(int(rl[0]),
                                                               int(rl[1]) + 1))
            allowed_numbers.update(range(int(rh[0]), int(rh[1]) + 1))
            cat_allowed_numbers[row.split(':')[0]].update(range(int(rh[0]),
                                                                int(rh[1]) + 1))
        elif ',' in row:
            all_pass.add(row.strip())
            for item in row.strip().split(','):
                if int(item) not in allowed_numbers:
                    tser += int(item)
                    invalid_pass.add(row.strip())
valid_pass = all_pass - invalid_pass
for pas in valid_pass:
    for i, item in enumerate(pas.split(',')):
        cats[i].append(int(item))
for key in cat_allowed_numbers.keys():
    for i, item in enumerate(cats):
        if set(item).issubset(cat_allowed_numbers[key]):
            print(key, i)

print('The answer to part 1 is: {}'.format(tser))



