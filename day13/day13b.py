buses = []


def targetfunc(t):
    timeprod = 1
    busprod = 1
    for bus in buses:
        busprod *= bus[0]
        timeprod *= (t + bus[1])
    return timeprod % busprod


with open('test.txt') as fi:
    teststr, datastr = fi.readlines()
data = datastr.split(',')
testnr = int(teststr)

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
print(buses)
print('The answer to part 1 is: {}'.format(store[0] * store[1]))
n = 0
divisor = 1
for bus in buses:
    divisor *= bus[0]


while True:
    n += divisor
    t = int(divisor ** (1.0 / len(buses)))
    while