class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #유클리디안 호제법
        def gcd(x,y):
            while(y):
                x,y = y,x%y
            return x

        if str1+str2 != str2+str1:
            return ''
        i = gcd(len(str1), len(str2))
        return str1[:i]