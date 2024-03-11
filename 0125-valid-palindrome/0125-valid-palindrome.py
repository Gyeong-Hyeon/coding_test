class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s, rev_s = '', ''
        for st in s:
            if not st.isalnum():
                continue
            lower = st.lower()
            new_s+=lower
            rev_s=lower+rev_s
        return new_s == rev_s