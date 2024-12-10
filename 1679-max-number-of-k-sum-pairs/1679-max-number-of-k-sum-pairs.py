class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        to_find, cnt = {}, 0
        
        for i, num in enumerate(nums):
            if found := to_find.get(num):
                cnt+=1
                found.pop()
                continue
            target = k-num
            to_find[target] = to_find.get(target,[]) + [i]
        return cnt