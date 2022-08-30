class Solution:
    def search(self, nums: List[int], target: int) -> int:
        max_idx = len(nums)
        min_idx = 0
        # for b in bin(len(nums))[::-1]:
        #     if b == 'b':
        #         break
        while True:
            mid_idx = int((max_idx+min_idx)/2)
            if nums[mid_idx] == target:
                return mid_idx
            if max_idx - min_idx <= 1:
                return -1
            elif nums[mid_idx] < target:
                min_idx = mid_idx
                continue
            else:
                max_idx = mid_idx
        # return -1