class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        1. Using a library
        from itertools import permutations
        return list(permutations(nums, len(nums)))
        
        2. Recursive
        nPn = n-1Pn-1 + n-2Pn-2       
        """
        def recursive(nums, perm=[], res=[]):
            if not nums: # -- NOTE [1] 
                res.append(perm[::]) #  -- NOTE [2] - append a copy of the perm at the leaf before we start popping/backtracking

            for i in range(len(nums)): # [1,2,3]
                newNums = nums[:i] + nums[i+1:]
                perm.append(nums[i])
                recursive(newNums, perm, res) # - recursive call will make sure I reach the leaf
                perm.pop() # -- NOTE [3] 
            return res
        return recursive(nums)