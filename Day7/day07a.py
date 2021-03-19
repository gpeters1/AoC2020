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

        new_contents = [bag[3:].replace(".","") if bag[1] != "1" else bag[3:].replace(".","")+"s" for bag in bag_dict[item]]
        new_bag_dict[item[:-1]] = new_contents
    return new_bag_dict
        

bag_dict = format_dict(data)
print(bag_dict)
new_bag_dict = remove_numbers_in_dict(bag_dict)
print("erf")
print(new_bag_dict)



def can_hold_shiny_gold(bag_dict):
    total_count = 0
    for bag in bag_dict:
        for allowed_bag in bag_dict[bag]:
            if allowed_bag == " other bags":
                continue
            if allowed_bag == "shiny gold bags":
                total_count += 1
                break
            count = test(allowed_bag, bag_dict)
            if count == 1:
                total_count += count
                break
    return total_count



def test(chosen_bag, bag_dict):
    contents = bag_dict[chosen_bag]
    for item in contents:
        if item == "shiny gold bags":
            return 1
        if item == " other bags":
            return 0
        count = test(item, bag_dict)
        if count == 1:
            return count
        
    return count


total_count = can_hold_shiny_gold(new_bag_dict)
print(total_count)