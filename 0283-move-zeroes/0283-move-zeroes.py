class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Requirements: Do not return anything, modify nums in-place instead.
        1. idx, cnt = 0
        2. if value = 0: cnt+1
        3. if value is not 0, change idx to idx-cnt
        4. if idx == len(nums)-1: break
        """
        idx, cnt = 0, 0
        while idx < len(nums):
            if nums[idx] == 0:
                cnt+=1
            else:
                nums[idx-cnt], nums[idx] = nums[idx], nums[idx-cnt]
            idx+=1
