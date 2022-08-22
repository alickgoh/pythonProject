num = int(input("Please enter first number:"))
check = 4
if num % 4 == 0:
    print(f"The number {num} is multiple of 4")
elif num % 2 == 0:
    print(f"The number {num} is even")
else:
    print(f"The number {num} is odd")