mem = dict()
masks = {''}


def createxmasks(mask, masks):
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


createxmasks('X0000000000011001111011101111011101X', masks)

with open('p14_input.txt') as fi:
    for item in fi.readlines():
        if item[:4] == 'mask':
            mask_a = mask_b = ''
            current_mask = item.split('mask = ')[1].strip()
            for ch in current_mask:
                if ch == 'X':
                    mask_a += '1'
                    mask_b += '0'
                elif ch == '0':
                    mask_a += '0'
                    mask_b += '0'
                else:
                    mask_a += '0'
                    mask_b += '1'
        else:
            number = int(item.split(' = ')[1].strip())
            number = int(mask_a, 2) & number
            number = int(mask_b, 2) ^ number
            adr = (item.split(' = ')[0].strip()).replace(']', '[').split('[')[1]
            mem[adr] = number
print('The answer to part 1 is: {}'.format(sum(mem.values())))
