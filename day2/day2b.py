with open('p2_input.txt') as fi:
    input_data = fi.read().splitlines()
    correct_count = 0
    for item in input_data:
        pos_1 = int(item.split()[0].split('-')[0])
        pos_2 = int(item.split()[0].split('-')[1])
        check_letter = item.split()[1][0]
        passwd = item.split()[2]
        if (passwd[pos_1 - 1] == check_letter) != \
                (passwd[pos_2 - 1] == check_letter):
            correct_count += 1
    print(correct_count)