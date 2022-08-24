class Solution:
    # def __init__(self, list1, list2):
    #     self.list1 = list1
    #     self.list2 = list2

    def addTwoNumbers(list1, list2):
        list1a = "".join(map(str, list1))
        list2a = "".join(map(str, list2))

        rvs1 = list1a[::-1]
        rvs2 = list2a[::-1]

        total = int(rvs1) + int(rvs2)
        print(total)


l1 = [2, 4, 3]
l2 = [5, 6, 4]

print(Solution.addTwoNumbers(l1, l2))
