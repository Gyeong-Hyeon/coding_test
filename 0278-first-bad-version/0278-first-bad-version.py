# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        * if version >= n, all bad
        * find what "bad" is within the range of int n
        1. Set a searching array from 1("low") to n("high")
        2. Check the result of api of middle value
         - If True: Move "high" to middle, save mid as bad
         - If False: Move "low" to middle+1
        3. If "low" is same with "high", return low
        """
        low, high = 1, n
        while low < high:
            mid = (low+high)//2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid+1
        return low