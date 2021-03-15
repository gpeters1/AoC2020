data = open("./Day6/day06.input").read().splitlines()
print(data)


def split(line):
    return [x for x in line]

total = 0
group_list = []
for line in data:
    if line == "":
        yes_per_group = len(set(group_list))
        total += yes_per_group
        group_list = []
    else:
        group_list.extend(split(line))

yes_per_group = len(set(group_list))
total += yes_per_group
group_list = []

print(total)