class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total, is_z = 1, -1
        for i in range(len(nums)):
            if nums[i] == 0:
                if is_z > -1:
                    return [0]*len(nums)
                is_z = i
                continue
            total*=nums[i]
        if is_z > -1:
            return [total if num == 0 else 0 for num in nums ]
        else:
            return [int(total/num) for num in nums]