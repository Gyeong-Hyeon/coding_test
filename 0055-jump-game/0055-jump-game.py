class Solution:
    def canJump(self, nums: List[int]) -> bool:
#         def jump(idx):
#             if idx == target:
#                 return True
#             if nums[idx] == 0 or idx > target:
#                 return False
            
#             next_idx = idx + nums[idx]
#             for i in range(idx+1, next_idx+1):
#                 if jump(i):
#                     return True
#             return False
        
#         target = len(nums)-1
#         return jump(0)
        pos = len(nums)-1
        for idx in range(len(nums)-1, -1, -1):
            if idx + nums[idx] >= pos:
                pos = idx
        return pos == 0