data = open("./Day9/day09.input").read().splitlines()
data = list(map(int, data))[:594]

answer = 258585477

def get_contiguous_set(data, answer):
    for i in range(len(data)):
        value_to_check = data[i]
        for j in range(i+1, len(data)):
            value_to_check += data[j]
            if value_to_check < answer:
                continue
            if value_to_check > answer:
                break
            if value_to_check == answer:
                return (i, j)


start, end = get_contiguous_set(data, answer)
contiguous_list = data[start:end+1]
final_answer = min(contiguous_list) + max(contiguous_list)
print(final_answer)

