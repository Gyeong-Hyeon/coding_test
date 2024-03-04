class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for st in strs:
            li = [0]*26
            for s in st:
                idx = ord(s)-97
                li[idx]+=1
            tp = tuple(li)
            ans[tp] = ans.get(tp,[]) + [st]
        return ans.values()