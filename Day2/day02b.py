passwords_with_policies = [i.strip() for i in open("day02.input")]


def number_of_correct_passwords(passwords_with_policies):
    count = 0
    for i in passwords_with_policies:
        split_array = i.split()
        number_of_letters = split_array[0].split("-")
        first_pos = int(number_of_letters[0]) - 1
        second_pos = int(number_of_letters[1]) - 1
        letter_for_password = split_array[1][0]
        password = split_array[2]
        if is_password_correct(first_pos, second_pos, letter_for_password, password):
            count += 1
    print(f"Number that are true is {count}")
        


def is_password_correct(min_number, max_number, letter_for_password, password):
    first_letter = password[min_number]
    second_letter = password[max_number]
    if first_letter == letter_for_password and second_letter != letter_for_password:
        return True
    if second_letter == letter_for_password and first_letter != letter_for_password:
        return True



number_of_correct_passwords(passwords_with_policies)

