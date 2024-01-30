name = input("What's your name? ")
age_str = input("How old are you? ")
is_celebrated_str = input("Did you celebrate your birthday already? (Y/N) ")

age = int(age_str)

if is_celebrated_str == "Y":
    birth_year = 2024 - age
else: 
    birth_year = 2024 - age - 1
    

message = "Hi " + name 
message += ", you are " + age_str 
message += " years old and you were born in " + str(birth_year)

print(message)
