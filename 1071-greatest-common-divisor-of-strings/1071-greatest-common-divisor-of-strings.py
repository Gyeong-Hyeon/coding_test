class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ''
        len1, len2 = len(str1), len(str2)
        for i in range(min(len1, len2), 0 , -1):
            if len1%i == 0 and len2%i == 0:
                return str1[:i]