def fibonacci():
    count = int(input("How many times to generate: "))
    a = 1
    b = 0
    cont = 1
    full_list = [1]
    while cont < count:
        total = b + a
        full_list.append(total)
        b = a
        a = total
        cont += 1
    return full_list


print(fibonacci())

# Alternate solution
# def gen_fib():
#     count = int(input("How many fibonacci numbers would you like to generate? "))
#     i = 1
#     if count == 0:
#         fib = []
#     elif count == 1:
#         fib = [1]
#     elif count == 2:
#         fib = [1, 1]
#     elif count > 2:
#         fib = [1, 1]
#         while i < (count - 1):
#             fib.append(fib[i] + fib[i-1])
#             i += 1
#     return fib
#
#
# print(gen_fib())
