class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Requirements: Do not return anything, modify nums in-place instead
        1) Basic two pointers
            1. idx, cnt = 0
            2. if value = 0: cnt+1
            3. if value is not 0, change idx to idx-cnt
            4. if idx == len(nums)-1: break
          Full code:
            cnt = 0
            for i in range(len(nums)):
                if nums[i] == 0:
                    cnt+=1
                    continue
                if count > 0:
                    nums[i-cnt], nums[i] = nums[i], nums[i-cnt]
        2) Another Two pointers
            1. set the point for first zero of the array (initial value is 0)
            2. rotate the array by index i from 1
            * note that zero pointer is always same or smaller than i because the pointer starts from 0 and i starts from 1 and both moves one per a loop             
            3. if nums[i] is not 0 and nums[pointer] is zero, swap the value at pointer
            4. if nums[pointer] is zero, we slow doesn't need to be increased.         
        """
        zero=0
        for i in range(1,len(nums)):
            if nums[i] != 0 and nums[zero] == 0:
                nums[zero], nums[i] = nums[i], nums[zero]
            if nums[zero] != 0:
                zero+=1
