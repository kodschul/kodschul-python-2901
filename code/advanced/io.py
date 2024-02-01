
with open('people.txt', 'r') as f:
    # read the whole content
    content = f.read()

    # read line by line
    # lines = f.readlines()

# convert the content to lines
lines = content.split("\n")

for name in lines:
    print(f"Hi {name.capitalize()}, what's up?")
