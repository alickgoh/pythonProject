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
        guess_duplicate_check = False
        while guess_duplicate_check is not True:
            guess = input(">>> ")
            if len(set(guess)) < len(answer):
                print("Digit cannot be duplicate")
            else:
                guess_duplicate_check = True

        if guess.isnumeric() and len(guess) == len(answer):
            if guess == answer:
                print(f"Congratulation, the answer is correct and your guess count is {guess_count}")
                guess_correctly = True
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
            break
        else:
            print("No alphabets and symbols allow!")


if __name__ == "__main__":
    cow_and_bulls()
    print('new branch testing')
