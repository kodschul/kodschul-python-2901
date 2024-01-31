number_guess = 5
remaining_attempts = 3
input_number = None

while input_number != number_guess and remaining_attempts > 0:
    input_number = int(input("Guess the number: "))

    if input_number == number_guess:
        break

    elif input_number > number_guess:
        print(f"Sorry, {input_number} is too high")

    elif input_number < number_guess:
        print(f"Sorry, {input_number} is too low")

    remaining_attempts -= 1

    if remaining_attempts > 0:
        print(f"You have {remaining_attempts} attempts left, think again!")

if input_number == number_guess:
    print(f"Congratulations! {input_number} is the correct number!")
else:
    print(f"Unfortunately you lost!")
