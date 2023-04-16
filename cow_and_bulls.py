import random


def cow_and_bulls():
    guess_count = 0
    guess_correctly = False
    answer = []

    while len(answer) != 4:
        answer = "".join(set(str(random.randint(1000, 9999))))

    print(f"secret code: {answer}")
    print("Welcome to the Cows and Bulls game!\nType 'Exit' to terminate the game\nEnter a number:")

    while guess_correctly is not True:
        guess_count += 1
        guess = ""

        while guess != answer:
            guess = input(">>> ")

            if guess.isnumeric() and len(guess) == len(answer):
                if guess == answer:
                    print(f"Congratulation, the answer is correct and your guess count is {guess_count}")
                    guess_correctly = True
                elif len(set(guess)) < 4:
                    print("Digit cannot be duplicate")
                else:
                    cow = 0
                    bulls = 0
                    for z in range(len(answer)):
                        if answer[z] == guess[z]:
                            cow += 1
                        elif answer[z] in guess:
                            bulls += 1
                    print(f"{cow} Cows, {bulls} Bulls")
            elif guess.isnumeric() and len(guess) != len(answer):
                print("Must be in 4 digit to play the guess game!")
            elif guess.lower() == "exit":
                print("Good Bye")
            else:
                print("No alphabets and symbols allow!")


if __name__ == "__main__":
    cow_and_bulls()

