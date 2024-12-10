class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = max_sum = sum(nums[:k])
        for start, end in zip(range(len(nums)-k+1),range(k,len(nums))):
            cur_sum = cur_sum-nums[start]+nums[end]
            if nums[start] < nums[end]:
                max_sum = max(max_sum, cur_sum)
        return max_sum/k