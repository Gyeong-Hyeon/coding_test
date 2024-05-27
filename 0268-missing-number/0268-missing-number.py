class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target = len(nums)*(len(nums)+1)/2
        input_sum = sum(nums)
        return int(target-input_sum)