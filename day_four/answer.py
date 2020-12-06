import re


class PassportVerifier(object):
    def __init__(self):
        self.fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}

    def execute(self):
        passports = self.get_passports()
        return self.verify_passports(passports)

    def get_passports(self):
        passports = []
        passport = dict()
        r = re.compile("([a-z]+)\\:([\\#a-z0-9]+)")
        f = open("input.txt", "r")
        for line in f:
            passport_data = r.findall(line)
            fields_data = self.get_passport_dict(passport_data)
            fields = fields_data.keys()
            if fields:
                passport.update(fields_data)
            else:
                passports.append(passport)
                passport = {}
        if passport:
            passports.append(passport)
        f.close()
        return passports

    def get_passport_dict(self, passport_data):
        # my naming is awful
        p = dict()
        for field, data in passport_data:
            p[field] = data
        return p

    def validate_fields(self):
        pass

    def verify_passports(self, grouped_passports):
        num_valid = 0
        for passport in grouped_passports:
            passport_fields = passport.keys()
            diff = set(passport_fields).symmetric_difference(self.fields)
            if diff != {'cid'} and diff != set():
                continue
            num_valid += self.is_valid(passport)
        return num_valid

    def is_valid(self, passport):
        byr = 1920 <= int(passport['byr']) <= 2002 and len((passport['byr'])) == 4
        iyr = 2010 <= int(passport['iyr']) <= 2020 and len((passport['iyr'])) == 4
        eyr = 2020 <= int(passport['eyr']) <= 2030 and len((passport['eyr'])) == 4
        hgt = self.is_height_valid(passport['hgt'])
        hcl = re.match("(\\#{1}[0-9a-f]{6})$", passport['hcl']) is not None
        ecl = len(passport['ecl']) == 3 and passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        pid = re.match("([0-9]{9})$", passport['pid']) is not None
        return False not in [byr, iyr, eyr, hgt, hcl, ecl, pid]

    def is_height_valid(self, height):
        is_valid = False
        if 'cm' in height and 150 <= int(height.split('cm')[0]) <= 193:
            is_valid = True
        elif 'in' in height and 59 <= int(height.split('in')[0]) <= 76:
            is_valid = True
        return is_valid


result = PassportVerifier().execute()
print(result)
