with open('p1_input.txt') as fi:
    in_data1 = [int(x) for x in fi.read().splitlines()]
    in_data2 = in_data1.copy()
    for item1 in in_data1:
        in_data2.pop(0)
        in_data3 = in_data2.copy()
        for item2 in in_data2:
            in_data3.pop(0)
            for item3 in in_data3:
                if item1 + item2 + item3 == 2020:
                    print(item1*item2*item3)
                    exit(0)
