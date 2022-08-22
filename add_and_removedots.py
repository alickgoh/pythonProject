def add_dots(string):
    return ".".join(string)


def remove_dots(string):
    return string.replace(".", "")


print(remove_dots("t.e.s.t"))


# the longer way
# def add_dots(s):
#     out = ""
#     for letter in s:
#         out += letter + "."
#     return out[:-1]
#
#
# def remove_dots(s):
#     out = ""
#     for letter in s:
#         if letter != ".":
#             out += letter
#     return out