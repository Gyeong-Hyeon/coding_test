class Solution:
    def reverse(self, x: int) -> int:
        """
        0. ë¤ì´ì¨ ì«ìê° 64ë¹í¸ê° ëì¼ë©´ return 0
        1. ë¶í¸ ê²ì¬ (is_negative), trueë©´ ë¶í¸ ë³ê²½
        [ì´í°ë ì´í° ê¸°ë¥ ì¬ì©]
            1. intë¥¼ strì¼ë¡ ë³ííê³  reverse
            2. reverseë ì«ìê° 34ë¹í¸ê° ëëì§ íì¸ -> ëì¼ë©´ return 0
            3. return int(is_negative+str)
        [ì«ìë¡ í´ê²°]
            1. ìì°¨ì ì¼ë¡ ë¬¸ìì´ì ì ì¥í  ë³ì ans ìì±
            2. x//10ì´ 0ì´ ë  ëê¹ì§ ë°ë³µë¬¸ ìí
            3. ë°ë³µë¬¸ ë´ìì x%10ì ansì ì¶ê°
            4. return int(is_negative+ans)
        """
        # ì«ìë¡ í´ê²°
        if 2**63 < x or -2**63 > x: return 0
        is_negative, ans = '', ''
        if x < 0:
            is_negative = '-'
            x*=-1
        while x//10 > 0:
            x, remainder = divmod(x, 10)
            ans+=str(remainder)
        ans+=str(x)
        if int(ans) > 2**31: return 0
        return int(is_negative+ans)