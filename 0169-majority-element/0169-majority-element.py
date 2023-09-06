class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for v in nums:
            if counter.get(v):
                counter[v]+=1
            else:
                counter[v] = 1
            if counter[v] > int(len(nums)/2):
                    return v