class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(nums, path, k, ret):
            if len(path) == k:
                ret.append(path)
                return
            
            for i in range(len(nums)):
                if len(nums)-i+len(path)>=k:  # Notice Here
                    dfs(nums[i+1:], path+[nums[i]], k, ret)
        
        r = []
        dfs(range(1, n+1), [], k, r)
        
        return r
        