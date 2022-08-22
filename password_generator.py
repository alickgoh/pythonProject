import string
import random


def password_generator(char_length):
    set1 = string.ascii_lowercase
    set2 = string.ascii_uppercase
    set3 = string.digits
    set4 = string.punctuation

    combined = "".join(set1 + set2 + set3 + set4)

    # the line below will generate 10 letters from combined randomly , k is the identifier for numbers of char to return
    return "".join(random.choices(combined, k=char_length))


print(password_generator(int(input('Please enter password length: '))))
