class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start, cnt, ans = 0, k, 0
        for i,num in enumerate(nums):
            if num:
                continue
            if cnt:
                cnt-=1
                continue
            if nums[start] == 0:
                start+=1
                continue
            ans = max(ans, i-start)
            while nums[start] == 1:
                start+=1
            start+=1
        return max(ans, i-start+1)