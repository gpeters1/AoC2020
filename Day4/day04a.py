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


def get_answer(passports):
    count = 0
    list_of_required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "ecl", "pid"]
    for i in passports:
        a = i.get("hcl")
        bb = [i.get(j) for j in list_of_required]
        print(bb)
        if not None in bb:
            count += 1
    return count



passports = list_of_passports(arr)
answer = get_answer(passports)
print(answer)
