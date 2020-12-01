infile = open('figures.txt', 'r')
numbers = [int(line) for line in infile.readlines()]

length = len(numbers)
num1 = 0
num2 = 0
for i in range(length):
    for j in range(length):
        sum = numbers[i] + numbers[j]
        if sum == 2020:
            num1 = numbers[i]
            num2 = numbers[j]
            break

print(f"The numbers are {num1} and {num2}")
multiply = num1 * num2
print(f"The answer is {multiply}")


num1 = 0
num2 = 0
num3 = 0
for i in range(length):
    for j in range(length):
        for k in range(length):
            sum = numbers[i] + numbers[j] + numbers[k]
            if sum == 2020:
                num1 = numbers[i]
                num2 = numbers[j]
                num3 = numbers[k]
                break

print(f"The numbers are {num1} and {num2} and {num3}")
multiply = num1 * num2 * num3
print(f"The answer to 1b is {multiply}")
