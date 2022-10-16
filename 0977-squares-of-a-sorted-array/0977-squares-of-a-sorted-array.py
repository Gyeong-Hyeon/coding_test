class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        start, end = 0, len(nums) - 1
        while start <= end:
            s_start, s_end = nums[start]**2, nums[end]**2
            if s_start > s_end:
                output[end - start] = s_start
                start+=1
            else:
                output[end - start] = s_end
                end-=1
        return output
    
