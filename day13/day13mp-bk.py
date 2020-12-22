import multiprocessing as mp
buses = list()
found = bool


def runcheck(n):
    buses = n[1:]
    n = n[0]
    for i in range(len(buses)):
        if (n + buses[i + 1][1] - buses[0][1]) % buses[i + 1][0] != 0:
            break
        elif i == len(buses) - 2:
            print('The answer to part 2 is: {}'.format(n - buses[0][1]))
            return True
        else:
            if i == len(buses) - 4:
                print(n)
            continue
    return False


if __name__ == '__main__':
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
    print('The answer to part 1 is: {}'.format(store[0] * store[1]))

    n = 0
    found = False
    while True:
        n += mp.cpu_count() * buses[0][0]
        jobs = [n - x*buses[0][0] for x in range(mp.cpu_count())]
        jobs = [[x] + buses for x in jobs]
        with mp.Pool(mp.cpu_count()) as p:
            if True in p.map(runcheck, jobs):
                p.terminate()
                exit()
