class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        [Condition & Constraints]
        1. numsìì valì´ë ëì¼í ììë¥¼ ëª¨ë ì ê±° í ë¨ì ììì ê°¯ìë¥¼ ë°í
        2. numsë in-placeë¡ ìì ëì´ì¼í¨
        3. numsìì valì ì ê±° í í ë¨ì ììë¤ì ëª¨ë ìì¼ë¡ ë¡ê¸°ë, numsì ê¸¸ì´ë ì ì§í´ì¼í¨
        3. numsì ê¸¸ì´ë 0ì¼ ì ìì
        4. valì´ numsìì ìì ì ìì

        [Pseudo code]
        1. numsì ê¸¸ì´ê° 0ì´ë©´ return 0
        2. í¬ì¸í°: nums ììì nums!=valì¸ ììë¥¼ ë®ì´ì¸ ìë¦¬
        3. nums[i] == val: ë¤ì ìì íì
        4. nums[i] != val: nums[ptr]ì nums[i]ë¥¼ ë®ì´ì°ê³  ptrì í ì¹¸ ë¤ë¡ ì®ê¹. ë¤ì ìì íì
        5. ptrë¶í° numsì ëê¹ì§ ë¹ ê°ì¼ë¡ ì±ì
        6. return len(nums) - ptr
        """

        if not nums:
            return 0
        ptr = 0
        for num in nums:
            if num != val:
                nums[ptr] = num
                ptr+=1
        return ptr