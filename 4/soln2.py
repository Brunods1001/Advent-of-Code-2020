import string
import sys

try:
    fname = sys.argv[1]
except IndexError:
    fname = 'input.txt'

with open(fname, 'r') as f:
    list_passports = f.read().split('\n\n')

# determine if each is valid
required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

num_valid = 0
for passport in list_passports:
    fields = passport.split()
    dict_f = dict(i.split(':') for i in fields)
    if required_fields != (set(dict_f.keys()) - set(['cid'])):
        continue
    val_byr = 1920 <= int(dict_f['byr']) <= 2002
    val_iyr = 2010 <= int(dict_f['iyr']) <= 2020
    val_eyr = 2020 <= int(dict_f['eyr']) <= 2030
    hgt = dict_f['hgt']
    hgt_unit = hgt[-2:]
    hgt_num = hgt[:-2]
    val_hgt = False
    if hgt_num.isnumeric():
        hgt_num = float(hgt_num)
        if hgt_unit == 'in':
            val_hgt = 59 <= hgt_num <= 76
        elif hgt_unit == 'cm':
            val_hgt = 150 <= hgt_num <= 193
    hcl = dict_f['hcl']
    allowed_hcl = set(string.ascii_lowercase[:6] + string.digits)
    val_hcl = hcl.startswith('#') and allowed_hcl.issuperset(
        hcl[1:]) and len(hcl) == 7
    allowed_ecl = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    val_ecl = allowed_ecl.issuperset([dict_f['ecl']])
    val_pid = len(dict_f['pid']) == 9 and dict_f['pid'].isnumeric()

    is_valid = val_byr and val_iyr and val_eyr and val_hgt and val_hcl and\
        val_ecl and val_pid
    num_valid += is_valid

print(num_valid)
