class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        cnt1, cnt2 = OrderedDict(sorted(Counter(word1).items())), OrderedDict(sorted(Counter(word2).items()))
        if Counter(cnt1.keys()) != Counter(cnt2.keys()):
            return False
        return Counter(cnt1.values()) == Counter(cnt2.values())