with open('test.txt') as fi:
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
print(buses)
for item in [x[0] for x in buses]:
    if item - testnr % item < waittime:
        waittime = item - testnr % item
        store = item, waittime
print('The answer to part 1 is: {}'.format(store[0]*store[1]))