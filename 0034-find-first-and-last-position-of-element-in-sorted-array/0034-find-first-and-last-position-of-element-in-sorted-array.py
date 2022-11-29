class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1,-1]
        
        start, end, ans = 0, len(nums)-1, []
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                if not ans:
                    ans = [mid, mid]
                if nums[start] == target and start < ans[0]:
                    ans[0] = start
                if nums[end] == target and end > ans[1]:
                    ans[1] = end
                start+=1
                end-=1
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid+1
        if not ans:
            return [-1,-1]
        else:
            return ans