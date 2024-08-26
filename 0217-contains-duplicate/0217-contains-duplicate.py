class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ht = {}
        for num in nums:
            if ht.get(num):
                return True
            ht[num] = 1
        return False