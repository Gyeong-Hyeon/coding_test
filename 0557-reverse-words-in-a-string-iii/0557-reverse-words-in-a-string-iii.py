class Solution:
    def reverseWords(self, s: str) -> str:
        """
        1) Pythonic way
            1. Split the string by empty space and put each word into a list
            2. Rotate the list
            3. Reverse each word
            4. After rotation, join the values of list with space
            Full code = return ' '.join([x[::-1] for x in s.split()])
        2) Two pointers
            1. set ans = '', start = 0
            2. Rotate s by index i
            3. If s[i] == ' ':
                ans+=s[start:i][::-1]
                ans+=' '
                start = i+1
            4. After rotation, add s[start:last idx][::-1] to ans once more because there's no traiiling spaces
        3) Use list
            1. set t='', ans = []
            2. Rotate the string
            3. If value == ' ', ans.append[t], t='' 
            4. Else, value+t
            5. After rotation, append t once more because there's no traiiling spaces in s
            6. join the values of list with space
        """
        t, ans = '', []
        for st in s:
            if st != ' ':
                t=st+t
                continue
            ans.append(t)
            t = ''
        ans.append(t)
        return ' '.join(ans)