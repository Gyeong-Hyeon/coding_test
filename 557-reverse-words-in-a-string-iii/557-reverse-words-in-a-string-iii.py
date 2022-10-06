class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        s = [st[::-1] for st in s]
        return ' '.join(s)
        