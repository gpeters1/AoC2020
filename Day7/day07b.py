data = open("./Day7/day07.input").read().splitlines()


def format_dict(data):
    bag_dict = {}
    for line in data:
        bag = line.split("contain")
        bag_contents = bag[1].split(",")
        bag_dict[bag[0]] = bag_contents
    return(bag_dict)


def remove_numbers_in_dict(bag_dict):
    new_bag_dict = {}
    for item in bag_dict:
        new_contents = [bag[1:].replace(".","") if bag[1] != "1" else bag[1:].replace(".","")+"s" for bag in bag_dict[item]]
        new_bag_dict[item[:-1]] = new_contents
    return new_bag_dict
        

bag_dict = format_dict(data)
new_bag_dict = remove_numbers_in_dict(bag_dict)



def recur_bag(selected_bag, bag_dict):
    bag_count = 0
    contents = bag_dict[selected_bag]
    for bag in contents:
        if bag == "no other bags":
            return 0
        multiplier = int(bag[:1])
        bag_to_search = bag[2:]
        bag_count += (multiplier * recur_bag(bag_to_search, bag_dict)) + multiplier
    return bag_count



bag_count = recur_bag("shiny gold bags", new_bag_dict)

print(bag_count)
