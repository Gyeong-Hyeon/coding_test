class Solution:
    def compress(self, chars: List[str]) -> int:
        cur_char, num, l = '', 0, len(chars)
        for _ in range(l+1):
            char = chars.pop(0)
            if char == cur_char:
                num+=1
                continue
            chars.append(cur_char)
            if num > 1:
                for n in str(num):
                    chars.append(n)
            cur_char, num = char, 1
        return len(chars)