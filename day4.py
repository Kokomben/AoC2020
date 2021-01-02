from day4input import *

input = input.split('\n\n')

def matches(value, acc):
    acc = list(acc)
    for c in value:
        if c not in acc:
            return False
    return True

def propervalidation(key, value):
    return(
        key == 'byr' and int(value) >= 1920 and int(value) <= 2002 or
        key == 'iyr' and int(value) >= 2010 and int(value) <= 2020 or
        key == 'eyr' and int(value) >= 2020 and int(value) <= 2030 or
        key == 'hgt' and (value[-2:] == 'cm' and int(value[:-2]) >= 150 and int(value[:-2]) <= 193 or value[-2:] == 'in' and int(value[:-2]) >= 59 and int(value[:-2]) <= 76) or
        key == 'hcl' and value[0] == '#' and len(value[1:]) == 6 and matches(value[1:], "abcdef0123456789") or 
        key == 'ecl' and value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] or
        key == 'pid' and len(value) == 9 and matches(value, "0123456789")
    )

maps = []
validMaps = []
for passport in input:
    passport = passport.replace('\n', ' ').split(' ')
    map = {
        'byr':False,
        'iyr':False,
        'eyr':False,
        'hgt':False,
        'hcl':False,
        'ecl':False,
        'pid':False,
        'cid':False,
    }
    validMap = map.copy()

    for datapoint in passport:
        splitted = datapoint.split(':')
        if len(splitted) > 1 and splitted[0] in map:
            map[splitted[0]] = True
            try:
                validMap[splitted[0]] = propervalidation(splitted[0], splitted[1])
            except:
                validMap[splitted[0]] = False

    maps.append(map)
    validMaps.append(validMap)


valid1 = 0
valid2 = 0
for map in maps:
    if map['byr'] and map['iyr'] and map['eyr'] and map['hgt'] and map['hcl'] and map['ecl'] and map['pid']:
        valid1 = valid1 + 1

for map in validMaps:
    if map['byr'] and map['iyr'] and map['eyr'] and map['hgt'] and map['hcl'] and map['ecl'] and map['pid']:
        valid2 = valid2 + 1
    

print(valid1)
print(valid2)