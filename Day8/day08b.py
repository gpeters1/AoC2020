import copy

data = open("./Day8/day08.input").read().splitlines()

def execute_game(data, score, step, steps_completed, end):
    if step == end:
        return score
    if step in steps_completed:
        return
    operation, argument = data[step].split()
    steps_completed.append(step)
    if operation == "nop":
        score = execute_game(data, score, step+1, steps_completed, end)
    if operation == "acc":
        score += int(argument)
        score = execute_game(data, score, step+1, steps_completed, end)
    if operation == "jmp":
        step += int(argument)
        score = execute_game(data, score, step, steps_completed, end)
    return score


def recur_until_fixed(data):
    end = len(data)
    i = 0
    while i < end:
        temp_copy = copy.deepcopy(data)
        operation, argument = temp_copy[i].split(" ")
        if operation == "nop":
            temp_copy[i] = "jmp" + " " + argument
            result = execute_game(temp_copy, 0, 0, [], end)
            if result is not None:
                return result
        if operation == "jmp":
            temp_copy[i] = "nop" + " " + argument
            result = execute_game(temp_copy, 0, 0, [], end)
            if result is not None:
                return result
        i += 1


print(recur_until_fixed(data))
