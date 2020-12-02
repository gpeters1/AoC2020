passwords_with_policies = [i.strip() for i in open("day02.input")]


def number_of_correct_passwords(passwords_with_policies):
    count = 0
    for i in passwords_with_policies:
        split_array = i.split()
        number_of_letters = split_array[0].split("-")
        min_number = number_of_letters[0]
        max_number = number_of_letters[1]
        letter_for_password = split_array[1][0]
        password = split_array[2]
        if is_password_correct(min_number, max_number, letter_for_password, password):
            count += 1
    print(f"Number that are true is {count}")
        


def is_password_correct(min_number, max_number, letter_for_password, password):
    number_of_occurences = password.count(letter_for_password)
    print(number_of_occurences)
    if int(min_number) <= number_of_occurences <= int(max_number):
        return True



number_of_correct_passwords(passwords_with_policies)