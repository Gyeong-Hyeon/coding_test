class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cnts = [False]*(len(nums)+1)        
        for num in nums:
            cnts[num] = True
        
        for i, cnt in enumerate(cnts):
            if not cnt:
                return i