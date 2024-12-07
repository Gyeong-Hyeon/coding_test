class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ''
        #모듈
        from math import gcd
        i = gcd(len(str1), len(str2))
        return str1[:i]