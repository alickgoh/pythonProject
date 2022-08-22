number = int(input("Please enter a number: "))

if number == 1 or number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
    if number == 2 or number == 3 or number == 5:
        print("Prime number")
    else:
        print("Is not Prime number")
else:
    print("Prime number")


# Alternate solution
# The line below take a range from 2 to userinput num then divide by modulus,
# if it cannot be divided to 0, it will return empty list
# num = int(input('Insert a number: '))
# a = [x for x in range(2, num) if num % x == 0]
#
#
# def is_prime(n):
#     if num > 1:
#         if len(a) == 0:
#             print('prime')
#         else:
#             print('Not prime')
#     else:
#         print('Not prime')
#
#
# is_prime(num)
