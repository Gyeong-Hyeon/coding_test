class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #ì¬ê·ë¥¼ ì´ì©í ë°©ë²
        ans, total_length = [], n*2
        def back_track(cur_str, opened, closed):
            #ì ì²´ ê´í¸ ìë¥¼ ë¤ ì¬ì©í ê²½ì°
            if len(cur_str) == total_length:
                ans.append(''.join(cur_str))
                return
            
            #ìì§ ì´ ì ìë ê´í¸ê° ë¨ììë ê²½ì°
            if opened < n:
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