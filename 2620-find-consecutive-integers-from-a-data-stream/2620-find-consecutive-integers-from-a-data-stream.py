class DataStream(object):
    def __init__(self, value, k):
        """
        :type value: int
        :type k: int
        """
        self.value = value
        self.k = k
        self.true_cnt = 0
        

    def consec(self, num):
        """
        :type num: int
        :rtype: bool
        1. íì¬ ê°ì´ valueì ê°ìì§ë¥¼ íì¸
        2. íì¬ ê°ì´ valueì ê°ë¤ë©´ true_cnt+=1
        3. true_cnt == k: k-=1, return True
        4. true_cnt != k : return False
        5. íì¬ ê°ì´ valueì ë¤ë¥´ë¤ë©´ true_cntë¥¼ 0ì¼ë¡ ì ííê³  return False
        """

        if num != self.value:
            self.true_cnt = 0
            return False
        self.true_cnt+=1
        if self.true_cnt == self.k:
            self.true_cnt-=1
            return True
        return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)