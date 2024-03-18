class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        st = []
        ht = {')':'(', '}':'{',']':'['}
        for c in s:
            if c in ['(','{','[']:
                st.append(c)
                continue
            if len(st) == 0:
                return False
            if not st.pop() == ht[c]:
                return False
        if len(st) > 0:
            return False
        return True