class Solution:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def addTwoNumbers(self):
        total = [self.list1 + self.list2 for self.list1, self.list2 in zip(self.list1, self.list2)]
        return total


l1 = [1, 2, 3]
l2 = [4, 5, 6]
Sol = Solution(l1, l2)
print(Sol.addTwoNumbers())
