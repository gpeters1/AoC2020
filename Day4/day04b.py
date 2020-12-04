arr = [i.strip() for i in open("day04.input")]

def list_of_passports(arr):
    dict1 = {}
    passports = []
    for i in range(len(arr)):
        if arr[i] == "":
            passports.append(dict1)
            dict1 = {}
        else:
            list1 = arr[i].split()
            for j in list1:
                key, value = j.split(":")
                dict1[key] = value
        if i == len(arr)-1:
            passports.append(dict1)

    return passports


def valid_birth(value):
    return 1920 <= int(value) <= 2002

def valid_issue(value):
    return 2010 <= int(value) <= 2020

def valid_expiry(value):
    return 2020 <= int(value) <= 2030

def valid_height(value):
    metric = value[-2:]
    if metric == "cm":
        return "150cm" <= value <= "193cm"
    if metric == "in":
        return "59in" <= value <= "76in"
    return False

def valid_hair(value):
    if len(value) == 7:
        if value[0] == '#':
            for i in range(1, 7):
                if value[i] not in ['a','b','c','d','e','f', '0','1','2','3','4','5','6','7','8','9']:
                    return False

            return True
    return False

def valid_eyes(value):
    return value in ['amb','blu','brn','gry','grn','hzl','oth']

def valid_pid(value):
    if len(value) == 9:
        for i in range(1,9):
            if value[i] not in ['0','1','2','3','4','5','6','7','8','9']:
                return False
        return True
    return False

def check_details(passport, passport_field):
    value = passport.get(passport_field)
    if value:
        if passport_field == "byr":
            return valid_birth(value)
        if passport_field == "iyr":
            return valid_issue(value)
        if passport_field == "eyr":
            return valid_expiry(value)
        if passport_field == "hgt":
            return valid_height(value)
        if passport_field == "hcl":
            return valid_hair(value)
        if passport_field == "ecl":
            return valid_eyes(value)
        if passport_field == "pid":
            return valid_pid(value)
    return False

def get_answer(passports):
    count = 0
    list_of_required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "ecl", "pid"]
    for passport in passports:
        bb = [check_details(passport, j) for j in list_of_required]
        if not False in bb:
            count += 1
    return count



passports = list_of_passports(arr)
answer = get_answer(passports)
print(answer)


