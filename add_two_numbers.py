class Solution:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def addTwoNumbers(self):
        list1a = "".join(map(str, self.list1))
        list2a = "".join(map(str, self.list2))

        rvs1 = list1a[::-1]
        rvs2 = list2a[::-1]

        total = int(rvs1) + int(rvs2)

        total = list(map(int, str(total)))
        return total[::-1]


l1 = [0,0]
l2 = [0]
Sol = Solution(l1, l2)
print(Sol.addTwoNumbers())
