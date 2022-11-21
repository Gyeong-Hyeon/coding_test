class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        discussion: https://leetcode.com/problems/triangle/discuss/2146264/C%2B%2B-Python-Simple-Solution-w-Explanation-or-Recursion-greater-DP
        """
        dp = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i + 1])

        return dp[0] 