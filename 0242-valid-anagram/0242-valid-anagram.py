class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        sht, tht = Counter(s), Counter(t)
        return sht == tht