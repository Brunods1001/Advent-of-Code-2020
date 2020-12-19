with open('input.txt', 'r') as f:
    list_passports = f.read().split('\n\n')

# determine if each is valid
required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

num_valid = 0
for passport in list_passports:
    fields = passport.split()
    keys, values = zip(*[i.split(':') for i in fields])
    common = set(keys) & required_fields
    num_valid += required_fields == common

print(num_valid)
