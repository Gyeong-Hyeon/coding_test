class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        while word1 and word2:
            ans+=(word1[0]+word2[0])
            word1, word2 = word1[1:], word2[1:]
        
        if rest:=(word1 or word2):
            ans+=rest
        return ans       