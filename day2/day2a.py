with open('p2_input.txt') as fi:
    input_data = fi.read().splitlines()
    correct_count = 0
    for item in input_data:
        min_nr = int(item.split()[0].split('-')[0])
        max_nr = int(item.split()[0].split('-')[1])
        range_letter = item.split()[1][0]
        passwd = item.split()[2]
        if passwd.count(range_letter) in range(min_nr, max_nr + 1):
            correct_count += 1
    print(correct_count)