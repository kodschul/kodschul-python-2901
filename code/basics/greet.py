name = input("What's your name? ")
age_str = input("How old are you? ")

age = int(age_str)
birth_year = 2024 - age

message = "Hi " + name 
message += ", you are " + age_str 
message += " years old and you were born in " + str(birth_year)

print(message)