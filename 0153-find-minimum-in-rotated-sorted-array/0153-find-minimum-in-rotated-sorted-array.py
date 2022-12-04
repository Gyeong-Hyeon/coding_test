class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans,start,end = nums[0], 0, len(nums)-1
        while start <= end:
            mid = (start+end)//2
            if nums[mid] > nums[end]:
                start = mid+1
            else:
                if ans <= nums[mid]:
                    return ans
                ans = nums[mid]
                end = mid-1
        return ans