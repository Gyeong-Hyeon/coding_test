class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target = len(nums)
        for i, num in enumerate(nums):
            target ^= i^num
        return target