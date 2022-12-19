class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1.  Make k to remainder after divided by len(nums) because if k is multiple of len(nums), it means full rotation, nums is same after rotation.
        The array after rotation is same with below:
        1) Reverse the array
        2) Reverse the array[:k] + reverse the array[-k:]
        
        Another solution: nums[-k:] + nums[:-k]
        """
        l = len(nums)
        k%=l
        if k == 0: pass
        nums.reverse()
        for i in range(k//2):
            nums[i], nums[k-i-1] = nums[k-i-1], nums[i]
        for i in range((l-k)//2):
            nums[k+i], nums[l-i-1] = nums[l-i-1], nums[k+i]
