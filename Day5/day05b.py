rows = (0, 128)
columns = (0, 8)


arr = [i.strip() for i in open("/Users/gregory.peters/BJSS/AOC2020/Day5/day05.input")]

print(arr)
def midpoint(numbers):
    return ((numbers[1] - numbers[0]) / 2) + numbers[0]

seat_id = 0
seats_taken = []
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
    seats_taken.append((int(rows[0]), int(columns[0])))



rows = (0, 128)
columns = (0, 8)
def create_all_seats(rows, columns):
    all_seats = []
    for i in range(rows[1]):
        for j in range(columns[1]):
            all_seats.append((i,j))
    return all_seats

all_seats = create_all_seats(rows,columns)


result = [elem for elem in all_seats if elem not in seats_taken ]



print((92*8) + 7)