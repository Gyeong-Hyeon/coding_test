class Solution:
    def decodeString(self, s: str) -> str:
        stat, priority, i = {}, 0, len(s)-1
        while i > -1:
            c = s[i]
            if c == ']':
                priority+=1
                i-=1
                continue
            if c.isalpha():
                stat[priority] = c + stat.get(priority, '')
                i-=1
                continue
            end = i-1
            while s[end].isnumeric():
                end-=1
            stat[priority-1] = stat.pop(priority,'')*int(s[end+1:i]) + stat.get(priority-1, '')
            priority-=1
            i = end
        return stat[0]