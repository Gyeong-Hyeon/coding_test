class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        [Conditions & Constraints]
        - ìë ¥ë°°ì´ë¤ì ê°ê° ì¤ë¦ì°¨ìì¼ë¡ ì ë ¬ëì´ìì.
        - ê° ììë ê°ì ìë ìì
        - num1ê³¼ num2ë ë¹ì´ìì ì ìì
        - m, n = ê° ìë ¥ë°°ì´ì ê¸¸ì´ (nums1ì në§í¼ 0ì´ ì¶ê°ë¡ ìì)
        - ìë¡ì´ ë°°ì´ì´ ìëë¼ nums1ìë¤ê° í©ì³ì¼í¨
        [Output]
        - nums1ì´ë nums2ë¥¼ ë³í©í´ì ì¤ë¦ì°¨ìì¼ë¡ ì ë ¬ë íëì ë°°ì´ì ë¦¬í´

        [pseudo code]
        1. not n1: n1ì´ë n2ê° ë¤ ë¹ì´ìì -> ê·¸ë¥ ë¦¬í´
        2. not n2: n1ì´ ì´ë¯¸ ì ëµ -> ê·¸ë¥ ë¦¬í´
        3. ans = []
        4. i=m-1ì´ê³  j=n-1ì¼ëê¹ì§:
        5. n1[i]ê° n2[j] ë³´ë¤ ìì¼ë©´: ans.append(n1[i]), i+=1
        6. n1[i]ê° n2[j]ë ê°ì¼ë©´: ans.extend([n1[i], n2[j]]), i+=1, j+=1
        7. n1[i]ê° n2[j] ë³´ë¤ í¬ë©´: ans.append(n2[j]), j+=1
        ---ë£¨í ë--
        8. i < m-1: n1ì ëë¨¸ì§ ììë¥¼ ansì append
        9. j < n-1: n2ì ëë¨¸ì§ ììë¥¼ ansì append
        10. for i in ans: n1[i] = ans[i]
        """

        if not nums1 or not nums2:
            return
        ans, i, j = [], 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                ans.append(nums1[i])
                i+=1
            elif nums1[i] > nums2[j]:
                ans.append(nums2[j])
                j+=1
            else:
                ans.extend([nums1[i],nums2[j]])
                i+=1
                j+=1
        
        # nums1ì í° ì«ìë¤ì´ ë¨ììë ê²½ì°
        while i < m:
            ans.append(nums1[i])
            i+=1
        # nums2ì í° ì«ìë¤ì´ ë¨ììë ê²½ì°
        while j < n:
            ans.append(nums2[j])
            j+=1
        
        # ansì ë´ê²¨ìë ì«ìë¤ì nums1ë¡ ì®ê¹
        for i, v in enumerate(ans):
            nums1[i] = v
        return