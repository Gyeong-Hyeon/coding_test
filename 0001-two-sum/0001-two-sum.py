class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for i in range(len(nums)):
            k = nums[i]
            rest = target - k
            if rest in ht.keys():
                return [ht[rest], i]
            ht[k] = i