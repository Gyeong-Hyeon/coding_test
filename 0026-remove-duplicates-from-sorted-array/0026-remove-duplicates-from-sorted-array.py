class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1, p2, l = 0,1,len(nums)
        while p2 < l:
            if nums[p1] == nums[p2]:
                p2+=1
                continue
            nums[p1+1] = nums[p2]
            p1+=1
            p2+=1
        return p1+1