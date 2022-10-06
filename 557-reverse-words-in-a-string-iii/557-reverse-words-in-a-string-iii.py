class Solution:
    def reverseWords(self, s: str) -> str:
        sp = s.split(' ')
        li_s = [st[::-1] for st in sp]
        return ' '.join(li_s)
        