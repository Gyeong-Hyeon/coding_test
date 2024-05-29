class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for num in nums:
            cnt[num] = cnt.get(num,0) + 1
        return sorted(cnt, key=lambda x: cnt[x], reverse=True)[:k]        