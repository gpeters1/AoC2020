data = open("./Day6/day06.input").read().splitlines()
data.append("")


def get_duplicates(group_list, person_list):
    group_set = set(group_list)
    person_set = set(person_list)
    group_set = group_set.intersection(person_set)
    return list(group_set)

def split(line):
    return [x for x in line]

total = 0
group_list = ["tagged"]
for line in data:
    if line == "":
        total += len(group_list)
        group_list = ["tagged"]
    else:
        if "tagged" in group_list:
            group_list.remove("tagged")
            group_list.extend(split(line))
        else:
            group_list = get_duplicates(group_list, set(split(line)))

print(total)