data = open("./Day9/day09.input").read().splitlines()
data = list(map(int, data))

PREAMBLE_LENGTH = 25

useable_numbers = data[:PREAMBLE_LENGTH]


def numbers_add_up(useable_numbers, data, index_of_total):
    for i in useable_numbers:
        for j in useable_numbers:
            if i == j:
                continue
            if data[index_of_total] - i - j == 0:
                useable_numbers.pop(0)
                useable_numbers.append(data[index_of_total])
                index_of_total += 1
                return numbers_add_up(useable_numbers, data, index_of_total)
    return data[index_of_total]




result = numbers_add_up(useable_numbers, data, PREAMBLE_LENGTH)
print(result)