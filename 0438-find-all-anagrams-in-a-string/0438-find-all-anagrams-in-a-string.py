class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # len(p) <= len(s) ?
        from collections import Counter
        ht, start, end, ans = Counter(list(p)), 0, 0, []
        while end < len(s):
            if ht.get(s[end]):
                ht[s[end]]-=1
                if end - start == len(p)-1:
                    ans.append(start)
                    ht[s[start]]+=1
                    start+=1
                end+=1
                continue
            for c in s[start:end]:
                if c == s[end]:
                    break
                ht[c]+=1
                start+=1
            start+=1
            end+=1
        return ans