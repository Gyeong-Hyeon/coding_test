class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sht, tht = {}, {}
        if len(s) != len(t):
            return False
        for st in s:
            sht[st] = sht.get(st,0)+1
        for st2 in t:
            tht[st2] = tht.get(st2,0)+1
        return sht == tht