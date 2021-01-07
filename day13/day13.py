import multiprocessing as mp
buses = list()
step = mp.cpu_count()
m = mp.Manager()
event = m.Event()
multiplier = 0


def runcheck(n, event):
    import itertools
    for j in itertools.count(n, step):
        item = j * multiplier
        if (j - n)/step % 1000 == 0:
            if event.is_set():
                return
        for i in range(len(buses) - 1):
            if (item + buses[i + 1][1] - buses[0][1]) % buses[i + 1][0] != 0:
                break
            elif i == len(buses) - 2:
                print('The answer to part 2 is: {}'.format(item - buses[0][1]))
                event.set()
            else:
                continue


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
    multiplier = buses[0][0]
    for item in [x[0] for x in buses]:
        if item - testnr % item < waittime:
            waittime = item - testnr % item
            store = item, waittime
    print('The answer to part 1 is: {}'.format(store[0] * store[1]))

    with mp.Pool(mp.cpu_count()) as p:
        p.starmap(runcheck, [(x, event) for x in range(mp.cpu_count())])
        p.close()
        event.wait()
        p.terminate()
        exit()
