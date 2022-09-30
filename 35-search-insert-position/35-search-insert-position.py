class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        max_idx = len(nums)
        min_idx = 0
        while True:
            mid_idx = int((max_idx+min_idx)/2)
            if nums[mid_idx] == target:
                return mid_idx
            if max_idx - min_idx <= 1:
                if nums[min_idx] > target:
                    return min_idx
                else:
                    return max_idx
            elif nums[mid_idx] < target:
                min_idx = mid_idx
                continue
            else:
                max_idx = mid_idx
        