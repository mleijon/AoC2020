def createxmasks(mask):
    masks = {''}
    for ch in mask:
        tmp_masks = set()
        for item in masks:
            if ch == '0':
                item += 'X'
                tmp_masks.add(item)
            elif ch == '1':
                item += '1'
                tmp_masks.add(item)
            else:
                item2 = item
                item += '1'
                item2 += '0'
                tmp_masks.update([item, item2])
        masks = tmp_masks
    return masks


mem = dict()

with open('p14_input.txt') as fi:
    for item in fi.readlines():
        if item[:4] == 'mask':
            current_mask = item.split('mask = ')[1].strip()
        else:
            for m in createxmasks(current_mask):
                mask_a = mask_b = ''
                for ch in m:
                    if ch == 'X':
                        mask_a += '1'
                        mask_b += '0'
                    elif ch == '0':
                        mask_a += '0'
                        mask_b += '0'
                    else:
                        mask_a += '0'
                        mask_b += '1'
                adr = int((item.split(' = ')[0].strip()).replace(']', '[').
                          split('[')[1])
                adr = int(mask_a, 2) & adr
                adr = int(mask_b, 2) ^ adr
                number = int(item.split(' = ')[1].strip())
                mem[adr] = number
print('The answer to part 2 is: {}'.format(sum(mem.values())))
