class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_num, prev_max_num = nums[0], 0
        for num in nums[1:]:
            cur_max = max(max_num, prev_max_num + num)
            prev_max_num, max_num = max_num, cur_max
        return cur_max
