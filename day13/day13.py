with open('p13_input.txt') as fi:
    teststr, datastr = fi.readlines()
data = datastr.split(',')
testnr = int(teststr)
buses = []
count = -1
for item in data:
    try:
        buses.append((int(item), count + 1))
        count += 1
    except:
        count += 1
        continue
waittime = 100000
store = tuple()
buses.sort(key=lambda x: x[0], reverse=True)
for item in [x[0] for x in buses]:
    if item - testnr % item < waittime:
        waittime = item - testnr % item
        store = item, waittime
print('The answer to part 1 is: {}'.format(store[0] * store[1]))
n = 0
while True:
    n += buses[0][0]
    for i in range(len(buses)):
        if (n + buses[i + 1][1] - buses[0][1]) % buses[i + 1][0] != 0:
            break
        elif i == len(buses) - 2:
            print('The answer to part 2 is: {}'.format(n - buses[0][1]))
            exit()
        else:
            if i == len(buses) - 4:
                print(n)
            continue
