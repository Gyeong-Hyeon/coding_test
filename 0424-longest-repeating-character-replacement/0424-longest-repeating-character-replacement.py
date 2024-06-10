class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, max_len, max_cnt, cnts = 0, 0, 0, {}
        for end in range(len(s)):
            cnts[s[end]] = cnts.get(s[end], 0) + 1
            max_cnt = max(max_cnt, cnts[s[end]])
            
            if end-start+1 > max_cnt+k:
                cnts[s[start]]-=1
                start+=1
            max_len = max(max_len, end-start+1)
        return max_len