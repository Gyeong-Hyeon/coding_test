class Solution:
    def climbStairs(self, n: int) -> int:
        """
        a=0 ~ 2a == n
        Sigma (n-a)!/a!(n-2a)!
        """
        def factorial(num):
            return num * factorial(num-1) if num > 1 else 1

        i, ans = 0, 0
        for i in range((n//2)+1):
            ans+=factorial(n-i)/(factorial(i)*factorial(n-(2*i)))
        return int(ans)
