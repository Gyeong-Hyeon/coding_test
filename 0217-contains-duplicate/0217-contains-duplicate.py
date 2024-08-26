class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        counter = Counter(nums)
        return True if any(val > 1 for val in counter.values()) else False