class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #ì¬ê·ë¥¼ ì´ì©í ë°©ë² (+pruning)
        ans = []
        def back_track(cur_str, opened, closed):
            #ë ì´ì ì´ ê´í¸ê° ìë ê²½ì°
            if opened == n:
                remained = ')' * (n-closed)
                ans.append(''.join(cur_str) + remained)
                return
            
            #ìì§ ì´ ì ìë ê´í¸ê° ë¨ììë ê²½ì°
            cur_str.append('(')
            back_track(cur_str, opened+1, closed)
            #ë¤ì ì°ì°ì ìí´ ì¶ê°í strì ê±°
            cur_str.pop()
            
            #ìì§ ë«ì ì ìë ê´í¸ê° ë¨ììë ê²½ì°
            if closed < opened:
                cur_str.append(')')
                back_track(cur_str, opened, closed+1)
                cur_str.pop()
        
        back_track([],0,0)
        return ans