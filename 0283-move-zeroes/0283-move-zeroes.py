class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cp=nums[:]
        idx=0
        for i in range(len(cp)):
            if cp[i] != 0:
                continue
            del nums[i-idx]
            idx+=1
            nums.append(0)