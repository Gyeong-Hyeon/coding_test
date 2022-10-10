class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ml=0
        for st in range(len(s)):
            ss=''
            e = st
            while s[e] not in ss:
                ss+=s[e]
                e+=1
                if e == len(s):
                    break
            if len(ss) > ml:
                ml=len(ss)
        return ml