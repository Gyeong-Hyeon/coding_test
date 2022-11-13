class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        1. We can use python list function
            s[:] = s[::-1]
        2. We can use two pointer algorithm
          1. Set first point and last point
          2. Swap the value of each point
          3. first move one to right, last move one to left
          4. Repeat 2 until first == last
        """
        l = len(s)-1
        for i in range(len(s)//2):
            s[i], s[l-i] = s[l-i], s[i]     
