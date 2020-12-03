arr = [i.strip() for i in open("day03.input")]

def get_input_array(arr):
    array = []
    for j in arr:
        j = [char for char in j]
        array.append(j)
    return array


def is_finished(array, position_y, position_x):
        if len(array) < position_y:
            return True

def duplicate(array, position_y, position_x):
    if len(array[0]) <= position_x:
        for i in range(len(array)):
            array[i] = array[i] + array[i]
    return array


def move(array, right, down):
    initial_position_x = 0
    initial_position_y = 0
    tree_count = 0
    for i in range(len(array)):
        if is_finished(array, initial_position_y, initial_position_x):
            break
        array = duplicate(array, initial_position_y, initial_position_x)
        if array[initial_position_y][initial_position_x] == '#':
            tree_count += 1
            array[initial_position_y][initial_position_x] = "O"
        initial_position_y = initial_position_y + down
        initial_position_x = initial_position_x + right
    
    return tree_count



a = move(get_input_array(arr), 1, 1)
b = move(get_input_array(arr), 3, 1)
c = move(get_input_array(arr), 5, 1)
d = move(get_input_array(arr), 7, 1)
e = move(get_input_array(arr), 1, 2)
part_b_answer = a * b * c * d * e
print(part_b_answer)
