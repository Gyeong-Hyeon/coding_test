class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ht = {}
        if len(s) != len(t):
            return False
        for st in s:
            ht[st] = ht.get(st,0)+1
        for st2 in t:
            if not ht.get(st2):
                return False
            ht[st2]-=1
        return True