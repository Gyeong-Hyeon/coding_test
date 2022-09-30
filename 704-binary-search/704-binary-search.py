class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_idx, max_idx = 0, len(nums)-1
        while max_idx >= min_idx:
            mid_idx = (max_idx+min_idx)//2
            if nums[mid_idx] == target:
                return mid_idx
            elif nums[mid_idx] < target:
                min_idx = mid_idx+1
                continue
            else:
                max_idx = mid_idx-1
        return -1