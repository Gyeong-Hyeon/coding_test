# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        * if version >= n, all bad
        * find what "bad" is within the range of int n
        1. Set a searching array from 1("low") to n+1("high")
        2. Check the result of api of middle value
         - If True: Move "high" to middle-1, save mid as bad
         - If False: Move "low" to middle+1
        3. If "low" is bigger than "high", return bad
        """
        low, high = 1, n+1
        while low <= high:
            mid = (low+high)//2
            if isBadVersion(mid):
                high, bad = mid-1, mid
            else:
                low = mid+1
        return bad