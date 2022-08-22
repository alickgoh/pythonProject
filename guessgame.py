import random


def rdn_guess():
    rdn = random.randint(1, 9)
    userinput = 0
    guess_count = 0
    while userinput != rdn and userinput != "exit":
        userinput = input("Please enter your guess between 1 to 9 : ")
        if userinput == "exit":
            break
        userinput = int(userinput)
        guess_count += 1
        if userinput < rdn:
            print("Too low")
        elif userinput > rdn:
            print("Too high")
        else:
            print(f"Exactly right!")
            print(f"Total guesses is {guess_count}")


rdn_guess()
