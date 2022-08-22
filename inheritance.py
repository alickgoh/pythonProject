class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def meow(self):
        print("meow")
    pass

dog1 = Dog()
cat1 = Cat()
dog1.bark()
cat1.walk()
cat1.meow()