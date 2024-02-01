class Animal:

    def __init__(self, name, age):
        print(f"A new animal was born, {name} ")
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi {self.name}, you're {self.age} y/o")


print("Animal class")

dog = Animal("dog", 5)
cat = Animal("cat", 3)

dog.greet()
cat.greet()


bmw = Car()

print(f"The car status: {bmw.status()}")
bmw.start()
print(f"The car status: {bmw.status()}")

bmw.stop()
print(f"The car status: {bmw.status()}")
