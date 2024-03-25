class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l, ans = len(nums), []
        for p1 in range(l-2):
            if p1 > 0 and nums[p1] == nums[p1-1]:
                continue
            if nums[p1] > 0:
                break
            target, p2, p3 = -nums[p1], p1+1, l-1
            while p2 < p3:
                s = nums[p2] + nums[p3]
                if s < target:
                    p2+=1
                    continue
                if s > target:
                    p3-=1
                    continue
                ans.append([nums[p1], nums[p2], nums[p3]])
                p2+=1
                p3-=1
                while p2 < p3 and nums[p2] == nums[p2-1]:
                    p2+=1
                while p2 < p3 and nums[p3] == nums[p3+1]:
                    p3-=1
        return ans
