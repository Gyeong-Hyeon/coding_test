class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''.join(filter(str.isalnum, s)).lower()
        return st == st[::-1]