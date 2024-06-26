class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        while start < end:
            while not s[start].isalnum():
                start+=1
                if start == len(s):
                    return True
            while not s[end].isalnum():
                end-=1
            if s[start].lower() != s[end].lower():
                return False
            start+=1
            end-=1
        return True