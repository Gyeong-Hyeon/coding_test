class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(self.factorial(m+n-2)/ (self.factorial(m-1)*self.factorial(n-1)))

    def factorial(self, i):
        return i*factorial(i-1) if i > 1 else 1