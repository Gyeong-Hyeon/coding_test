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
            1. set t='', ans=[]
            2. Rotate the string
            3. If value == ' ', ans.append[t], t='' 
            4. Else, value+t
            5. After rotation, append t once more in case there wasn't whiespace at the end of "s"
            6. join the values of list with space
        """
        t, ans = '', []
        for st in s:
            if st == ' ':
                ans.append(t)
                t = ''
                continue
            t=st+t
        if t:
            ans.append(t)
        return ' '.join(ans)