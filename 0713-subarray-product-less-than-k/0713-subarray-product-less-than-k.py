class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        s, e, ans, prod = 0, 0, 0, 1
        while e < len(nums):
            prod*=nums[e]
            if prod < k:
                ans+=(e-s+1)
                e+=1
                continue
            if e > s:
                prod = prod / (nums[s]*nums[e])
            else:
                prod = prod / nums[e]
                e+=1
            s+=1
        return ans