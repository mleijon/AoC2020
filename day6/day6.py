with open('p6_input.txt') as fi:
    count = 0
    answers1 = [x.replace('\n', '') for x in fi.read().split('\n\n')]
    fi.seek(0)
    answers2 = [x.split('\n') for x in fi.read().split('\n\n')]
    for item in answers1:
        count += len(set(item))
    print('The answer to part 1 is: {}'.format(count))
    count = 0
    for group in answers2:
        common_answers = set(group[0])
        for person in group:
            common_answers = set(common_answers).intersection(set(person))
        count += len(common_answers)
    print('The answer to part 2 is: {}'.format(count))