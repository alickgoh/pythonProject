class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)[::-1]
        if str(x) != y:
            return False
        return True

    print(isPalindrome(10, 101))