class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        * Why the description says "non-decreasing" order, not "increasing" order?
         - Maybe there could be same numbers
         1) If the first value is neg, it's the biggest val among all neg vals in the array after squaring.
         2) The last value is the biggest val among all pos vals in the array
         3) We need to compare two values and move pointers based on the result of comparing. So need to use Two pointer algorithm
         
         1. Set left = 0, right = last value idx, idx = new array idx, first value is same with right
         2. Compare the square of left and the square of right
            - If left > right, put the square of left in the new array[idx] and left+1
            - Else, put the squre of right in the new array[idx] and right -1
            - idx-1
         3. Repeat 2 until idx == 0. If idx == -1, return the new array.
        """
        ans, left, right, idx = [0]*len(nums), 0, len(nums)-1, len(nums)-1
        left_val, right_val = nums[left]**2, nums[right]**2
        while idx >= 0:
            if left_val > right_val:
                ans[idx] = left_val
                left+=1
                left_val = nums[left] **2
            else:
                ans[idx] = right_val
                right-=1
                right_val = nums[right]**2
            idx-=1
        return ans