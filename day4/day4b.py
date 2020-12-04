with open('p4_input.txt') as fi:
    count = 0
    allowed_chars = set('abcdef0123456789')
    allowed_digits = allowed_chars - set('abcdef')
    allowed_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    in_data = fi.read().split('\n\n')
    for item in in_data:
        byr = 'byr' in item
        pid = 'pid' in item
        eyr = 'eyr' in item
        hgt = 'hgt' in item
        iyr = 'iyr' in item
        ecl = 'ecl' in item
        hcl = 'hcl' in item
        cid = 'cid' in item
        if byr and pid and eyr and hgt and iyr and ecl and hcl:
            byr_OK = iyr_OK = eyr_OK = hgt_OK = False
            pid_OK = ecl_OK = hcl_OK = False
            byr_value = int(item.split('byr:')[1].split()[0])
            iyr_value = int(item.split('iyr:')[1].split()[0])
            eyr_value = int(item.split('eyr:')[1].split()[0])
            hgt_value = item.split('hgt:')[1].split()[0]
            hcl_value = item.split('hcl:')[1].split()[0]
            ecl_value = item.split('ecl:')[1].split()[0]
            pid_value = item.split('pid:')[1].split()[0]
            if 1920 <= byr_value <= 2002:
                byr_OK = True
            if 2010 <= iyr_value <= 2020:
                iyr_OK = True
            if 2020 <= eyr_value <= 2030:
                eyr_OK = True
            if 'in' in hgt_value and 59 <= int(hgt_value.split('in')[0]) <= 76:
                hgt_OK = True
            if 'cm' in hgt_value and 150 <= int(hgt_value.split('cm')[0])\
                    <= 193:
                hgt_OK = True
            if hcl_value[0] == '#' and len(hcl_value) == 7 and \
                    set(hcl_value[1:]).issubset(allowed_chars):
                hcl_OK = True
            if ecl_value in allowed_ecl:
                ecl_OK = True
            if len(pid_value) == 9 and set(pid_value).issubset(allowed_digits):
                pid_OK = True
            if byr_OK and iyr_OK and eyr_OK and hgt_OK and hcl_OK and ecl_OK\
                    and pid_OK:
                count += 1
    print(count)
