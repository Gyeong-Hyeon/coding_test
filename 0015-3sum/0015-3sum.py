class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans, n = [], len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target, start, end = nums[i]*-1, i+1, n-1
            while start < end: #start to find target
                if nums[start] + nums[end] == target:
                    ans.append([nums[i],nums[start],nums[end]])
                    start+=1
                    while start < end and nums[start] == nums[start-1]:
                        start+=1
                elif nums[start] + nums[end] < target:
                    start+=1
                else:
                    end-=1
        return ans   