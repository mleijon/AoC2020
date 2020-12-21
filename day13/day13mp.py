import multiprocessing as mp
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
buses.sort(key=lambda x: x[0], reverse=True)
for item in [x[0] for x in buses]:
    if item - testnr % item < waittime:
        waittime = item - testnr % item
        store = item, waittime
print('The answer to part 1 is: {}'.format(store[0] * store[1]))



def runcheck(n):
    global found
    for i in range(len(buses)):
        if (n + buses[i + 1][1] - buses[0][1]) % buses[i + 1][0] != 0:
            break
        elif i == len(buses) - 2:
            print('The answer to part 2 is: {}'.format(n - buses[0][1]))
            p.close()
            found = True
        else:
            continue


n = 0
found = False
while not found:
    n += mp.cpu_count() * buses[0][0]
    jobs = [n - x*buses[0][0] for x in range(mp.cpu_count())]
    with mp.Pool(mp.cpu_count()) as p:
        p.map(runcheck, jobs)



