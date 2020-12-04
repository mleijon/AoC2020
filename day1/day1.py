with open('p1_input.txt') as fi:
    in_data1 = [int(x) for x in fi.read().splitlines()]
    in_data2 = in_data1.copy()
    part1_done = part2_done = False
    for item1 in in_data1:
        in_data2.pop(0)
        in_data3 = in_data2.copy()
        for item2 in in_data2:
            in_data3.pop(0)
            for item3 in in_data3:
                if item1 + item2 == 2020:
                    if not part1_done:
                        print('The answer to part 1 is: {}'.
                              format(item1*item2))
                        part1_done = True
                elif item1 + item2 + item3 == 2020:
                    if not part2_done:
                        print('The answer to part 2 is: {}'.
                              format(item1*item2*item3))
                        part2_done = True
                if part1_done and part2_done:
                    exit()

