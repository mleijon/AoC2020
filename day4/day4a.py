with open('p4_input.txt') as fi:
    count = 0
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
        count += byr and pid and eyr and hgt and iyr and ecl and hcl
    print(count)
