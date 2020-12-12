from collections import defaultdict
import copy

with open('p10_input.txt') as fi:
    data = [int(x.strip()) for x in fi.readlines()]
    count_1 = count_3 = 0
    data.append(0)
    data.sort()
    data.append(data[-1] + 3)
    for i in range(0, len(data) - 1):
        if data[i+1] - data[i] == 1:
            count_1 += 1
        elif data[i+1] - data[i] == 3:
            count_3 += 1
print('The answer to part 1 is: {}'.format(count_1*count_3))
adapters = defaultdict(lambda: 0)
adapters[0] = 1
complete_chains = False
count = 0


def build_chain(adapters):
    global count
    new_adapters = defaultdict(lambda: 0)
    for adapter in data:
        for key in adapters.keys():
            if 1 <= adapter - key <= 3:
                new_adapters[adapter] += adapters[key]
                if adapter == data[-1]:
                    count += adapters[key]
    adapters = copy.deepcopy(new_adapters)
    if len(adapters) == 1 and list(adapters.keys())[0] == data[-1]:
        print('The answer to part 2 is: {}'.format(count))
    else:
        build_chain(adapters)


build_chain(adapters)
