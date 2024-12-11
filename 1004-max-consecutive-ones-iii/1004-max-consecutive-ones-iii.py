class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        while k and i < len(nums):
            if not nums[i]:
                k-=1
            i+=1

        ans, start = i, 0
        while i < len(nums):
            if not nums[i]:
                ans = max(ans, i-start)
                if nums[start]:
                    while nums[start]:
                        start+=1
                start+=1
            i+=1
        return max(ans, i-start)