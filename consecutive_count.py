# def consecutive_zeros(numbers):
#     result = 0
#     cnt = 0
#     for i in numbers:
#         if i == "0":
#             cnt += 1
#         else:
#             cnt = 0
#         result = max(result, cnt)
#     return result
#
#
# print(consecutive_zeros("100111101000000110"))


def consecutive_zeros(bin_str):
    # bin_str.split('1') is used to remove 1 from the string and display only zeros in the list
    # and then the max is used to choose the max in length of the zeros from the list
    return max([len(zero) for zero in bin_str.split("1")])


print(consecutive_zeros("1001111010000110"))
