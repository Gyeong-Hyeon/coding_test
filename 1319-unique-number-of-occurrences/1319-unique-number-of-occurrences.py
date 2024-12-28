class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ht = {}
        for num in arr:
            ht[num] = ht.get(num,0) + 1
        vals = ht.values()
        return len(vals) == len(list(set(vals)))