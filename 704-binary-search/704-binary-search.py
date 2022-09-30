class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_idx, max_idx = 0, len(nums)
        min_idx = 0
        while True:
            mid_idx = (max_idx+min_idx)//2
            if nums[mid_idx] == target:
                return mid_idx
            if max_idx - min_idx <= 1:
                return -1
            elif nums[mid_idx] < target:
                min_idx = mid_idx
                continue
            else:
                max_idx = mid_idx