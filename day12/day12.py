with open('p12_input.txt') as fi:
    data = [(x[0], int(x[1:].strip())) for x in fi.readlines()]
