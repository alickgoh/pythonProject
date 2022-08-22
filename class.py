class Person:
    def __init__(self, fname, sname):
        self.fname = fname
        self.sname = sname

    def talk(self):
        print(f"I am {self.fname} {self.sname}")


name1 = Person("James", "Bond")
name2 = Person("Bob", "Marley")
name1.talk()
name2.talk()
