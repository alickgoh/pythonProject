def format_number(number):
    # if number >= 1000:
    #     rvs_number = str(number)[::-1]
    #     for i in range(len(rvs_number)):
    #         k = 3
    #         rvs_number_comma = rvs_number[:k] + "," + rvs_number[k:]
    #
    #         str_number = rvs_number_comma[::-1]
    #
    #     print(str_number)
    # else:
    #     print(number)
    print(f"{number:,d}")
    print('{:,}'.format(number))


format_number(1000000)

