class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r, cnt = 0, len(nums)-1, 0
        
        while l < r:
            target = nums[l]+nums[r]
            if target < k:
                l+=1
                continue
            if target > k:
                r-=1
                continue
            cnt+=1
            l+=1
            r-=1
        return cnt