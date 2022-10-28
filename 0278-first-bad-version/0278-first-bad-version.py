# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        max_bad = n
        min_bad = 1
        while True:
            mid_bad = round((max_bad+min_bad)/2+0.1)
            if not isBadVersion(mid_bad-1) and isBadVersion(mid_bad):
                return mid_bad
            if max_bad == mid_bad:
                return min_bad
            elif isBadVersion(mid_bad):
                max_bad = mid_bad
            else:
                min_bad = mid_bad        