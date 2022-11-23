class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        1. To use only constant extra space, we can't store the frequency of each element.
        2. XOR has below properties:
            - xor of a same number with it self is zero.
            - xor is commutative.
            - xor of any number with 0 is the number itself.
        That means if a^b^c^b^a == a^a^b^b^c == 0^0^c == 0^c == c and this expression applies regardless of the number of elements in the list.
        """
        if len(nums) == 1: return nums[0]
        ans = 0
        for i in nums:
            ans^=i
        return ans        