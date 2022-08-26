def capital_indexes(self):
    b = []
    for x in range(len(self)):
        if self[x].isupper() is True:
            b.append(x)
    return b


print(capital_indexes("TEsT"))


# Alternate short solution
def capital_indexes(self):
    return [i for i in range(len(self)) if self[i].isupper()]


print(capital_indexes("TEsT"))