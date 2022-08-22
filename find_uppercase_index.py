def capital_indexes(self):
    b = []
    for x in self:
        if x.isupper() is True:
            b.append(self.index(x))
    print(b)


capital_indexes("HeLlO")