class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """
        1. Rotate the string one by one
        2. If the char is digit, keep adding it to the original string
        3. Else, make two options, uppercase and lowercase, and add each option after the substrings stored so far.
        """
        ans = ['']
        for c in s:
            if c.isalpha():
                ans = [perm+opt for perm in ans for opt in [c.upper(), c.lower()]]
            else:
                ans = [perm+c for perm in ans]
        return ans