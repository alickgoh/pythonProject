def convert(a):
    return [str(b) for b in a]


print(convert([1, 2, 3]))


# using map
def convert1(ns):
    return list(map(str, ns))


print(convert1([1, 2, 3]))
