data = open("./Day8/day08.input").read().splitlines()


ops = {"+": lambda x: x, "-": lambda x: -x}

def execute_game(data, score, step, steps_completed):
    operation, argument = data[step].split(" ")
    if step in steps_completed:
        return score
    steps_completed.append(step)
    if operation == "nop":
        score = execute_game(data, score, step+1, steps_completed)
    if operation == "acc":
        score += ops[argument[:1]] (int(argument[1:]))
        score = execute_game(data, score, step+1, steps_completed)
    if operation == "jmp":
        step += ops[argument[:1]] (int(argument[1:]))
        score = execute_game(data, score, step, steps_completed)
    return(score)


print(execute_game(data, 0, 0, []))