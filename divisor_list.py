def divisor(num):
    divisor_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor_list.append(i)
    return divisor_list


print(divisor(int(input("Please input a number: "))))
