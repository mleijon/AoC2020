import multiprocessing as mp


def runcheck(n):
    buses = n[1]
    data = n[0]
    for item in data:
        for i in range(len(buses)):
            if (item + buses[i + 1][1] - buses[0][1]) % buses[i + 1][0] != 0:
                break
            elif i == len(buses) - 2:
                print('The answer to part 2 is: {}'.format(item - buses[0][1]))
                return True
            else:
                # if i == len(buses) - 3:
                #     print(item)
                continue
    return False


if __name__ == '__main__':
    with open('test.txt') as fi:
        teststr, datastr = fi.readlines()
    data = datastr.split(',')
    testnr = int(teststr)
    count = -1
    buses = list()
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
    mult = 1000
    m = mult * mp.cpu_count()
    while True:
        n += 1
        jobs_all = [(n*m - x)*buses[0][0] for x in range(m)]
        jobs = list()
        for x in range(mp.cpu_count()):
            job = list()
            job.append(jobs_all[x * mult:(x + 1) * mult])
            job.append(buses)
            jobs.append(job)
        with mp.Pool(mp.cpu_count()) as p:
            if True in p.map(runcheck, jobs):
                p.terminate()
                exit()
