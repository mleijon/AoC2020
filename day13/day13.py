with open('p13_input.txt') as fi:
    teststr, datastr = fi.readlines()
data = datastr.split(',')
testnr = int(teststr)
buses = []
for item in data:
    try:
        buses.append(int(item))
    except:
        continue
waittime = 100000
store = tuple()
for item in buses:
    if item - testnr % item < waittime:
        waittime = item - testnr % item
        store = item, waittime
print('The answer to part 1 is: {}'.format(store[0]*store[1]))