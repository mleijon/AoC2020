with open('p9_input.txt') as fi:
    data = [int(x.strip()) for x in fi.readlines()]


def sum_all_pairs(inp_lst):
    out_lst = set()
    nr_nr = len(inp_lst)
    for i in range(1, nr_nr):
        for item in inp_lst[i:]:
            out_lst.add(inp_lst[i - 1] + item)
    return out_lst


start = 25
current_sum = target_sum = 0
for i in range(start, len(data)):
    if data[i] not in sum_all_pairs(data[start - 25:i]):
        print('The answer to part 1 is: {}'.format(data[i]))
        target_sum = data[i]
        break
start = - 1
while True:
    start += 1
    current_sum = 0
    min_val = 1E100
    max_val = -1
    for i in range(start, len(data)):
        current_sum += data[i]
        max_val = max(max_val, data[i])
        min_val = min(min_val, data[i])
        if current_sum >= target_sum:
            break
    if current_sum == target_sum:
        break
print('The answer to part 2 is: {}'.format(min_val + max_val))
