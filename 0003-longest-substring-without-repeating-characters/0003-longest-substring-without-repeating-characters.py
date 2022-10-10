class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        sub_str = ''
        max_len = 0
        for c in s:
            if c in sub_str:
                if max_len < len(sub_str):
                    max_len = len(sub_str)
                idx = sub_str.find(c)
                sub_str = sub_str[idx+1:]
            sub_str+=c
        return max(max_len, len(sub_str))