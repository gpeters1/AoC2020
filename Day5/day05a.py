rows = (0, 128)
columns = (0, 8)

combination1 = "FBFBBFFRLR"
combination2 = "BFFFBBFRRR"
combination3 = "FFFBBBFRRR"
combination4 = "BBFFBBFRLL"

arr = [i.strip() for i in open("/Users/gregory.peters/BJSS/AOC2020/Day5/day05.input")]

print(arr)
def midpoint(numbers):
    return ((numbers[1] - numbers[0]) / 2) + numbers[0]

seat_id = 0
for j in arr:
    rows = (0, 128)
    columns = (0, 8)
    for i in j:
        if i == "F":
            rows = (rows[0], midpoint(rows))
        if i == "B":
            rows = (midpoint(rows), rows[1])
        if i == "L":
            columns = (columns[0], midpoint(columns))
        if i == "R":
            columns = (midpoint(columns), columns[1])
    if seat_id < rows[0] * 8 + columns[0]:
        seat_id = rows[0] * 8 + columns[0]
