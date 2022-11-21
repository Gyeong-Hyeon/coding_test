class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Return the maximum sum of not adjacent values.
        
        Total values we can select is round(len(count))
        By rotating the array, find the maximum value, and rotating the array except the adjacent values, find the next maxmum value,..
        repeat until find round(len(count)) values.
        
        discuss: https://leetcode.com/problems/house-robber/discuss/1605797/C%2B%2BPython-4-Simple-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP
        """
        prev2, prev, cur = 0,0,0
        for i in nums:
            cur = max(prev, i + prev2)
            prev2 = prev
            prev = cur
        return cur