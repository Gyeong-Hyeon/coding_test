class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target = set(i for i in range(len(nums)+1))
        nums = set(nums)
        return list(target-nums)[0]