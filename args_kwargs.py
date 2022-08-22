def adder(*args):
    print(sum(args))


adder(1, 2, 3, 4)
adder(3, 4, 5, 1, 2, 3, 4, 7)


def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))


intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890, Country="Kakashi")
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)