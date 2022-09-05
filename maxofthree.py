class Count:
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def max_of_three(self):
        if (self.arg1 > self.arg2) and (self.arg1 > self.arg3):
            max_number = self.arg1
        elif (self.arg2 > self.arg1) and (self.arg2 > self.arg3):
            max_number = self.arg2
        elif (self.arg3 > self.arg1) and (self.arg3 > self.arg2):
            max_number = self.arg3
        return max_number

    def max_using_max(self):
        return max(self.arg1, self.arg2, self.arg3)


c = Count(3, 9, 5)
print(c.max_of_three())

#
# k = Count(3, 4, 5)
# print(k.max_using_max())
