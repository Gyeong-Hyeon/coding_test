class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        ht = {')':'(', '}':'{',']':'['}
        for c in s:
            if c in ht.values():
                st.append(c)
                continue
            if len(st) == 0 or st.pop() != ht[c]:
                return False
        return not st