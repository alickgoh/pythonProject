import random

num_len = 4
number_list = random.randint(1000, 9999)
number = str(number_list)
cow = 0
print(number_list)
while cow < num_len:
    cow = 0
    bull = 0
    validity = 0

    guess = input("Enter your number  :")

    for i in guess:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and len(guess) == num_len:
            validity = validity + 1

    if validity == num_len:
        for i in range(num_len):
            if number[i] == guess[i]:
                cow = cow + 1
            elif number[i] in guess:
                bull = bull + 1

        if cow == num_len:
            win = " __Yeah You Guess it correct__ !!!"
        else:
            win = "__Try again__ !!"
        print("cows :", cow, ", bulls :", bull, win)

    else:
        print("__Please enter a valid number")