class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def delChar(st, p, cnt):
            while p >= 0:
                if st[p] == '#':
                    cnt+=1
                    p-=1

                elif cnt > 0:
                    cnt-=1
                    p-=1

                else:
                    return p, cnt
            return p, cnt
            
        ps, pt, cnt_s, cnt_t = len(s)-1, len(t)-1, 0, 0
        while ps >= 0 or pt >= 0:
            ps, cnt_s = delChar(s, ps, cnt_s)
            pt, cnt_t = delChar(t, pt, cnt_t)
            
            if ps >= 0 and pt >= 0 and s[ps] != t[pt]:
                return False
            if (ps>=0) != (pt>=0):
                return False
            
            ps-=1
            pt-=1
        return True