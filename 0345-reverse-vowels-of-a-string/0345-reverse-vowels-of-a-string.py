class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels, stack = ('a','e','i','o','u'), []        
        for c in s:
            if c.lower() in vowels:
                stack.append(c)
        if not stack:
            return s
        
        ans = ''
        for c in s:
            if c.lower() in vowels:
                ans+=stack.pop()
            else:
                ans+=c
        return ans