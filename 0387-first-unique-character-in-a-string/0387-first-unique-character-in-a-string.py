class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        state, ans = [0]*26, 0
        for c in s:
            idx = ord(c)-97
            state[idx]+=1

        for i, c in enumerate(s):
            idx = ord(c)-97
            if state[idx] == 1:
                return i
        return -1