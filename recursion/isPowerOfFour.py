class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def recursion(x):
            if n == 1 or x == n:
                return True
            if x < n:
                return recursion(x*4)
            return False
        return recursion(1)