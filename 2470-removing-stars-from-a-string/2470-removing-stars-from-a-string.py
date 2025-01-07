class Solution:
    def removeStars(self, s: str) -> str:
        ans = ''
        for c in s:
            if c != '*':
                ans+=c
                continue
            ans = ans[:-1]
        return ans