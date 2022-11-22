class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        1. Bit manipulation
            n&n-1 manipulation replaces the rightmost 1 in n with a 0 and leaves the remaining 1s and 0s
            because n is (000...)1...00...1 and n-1 is (000...)1...00...0 so the result is (000...)1...00...0.
            Therefore, when we repeat the manipulation and add 1 to count each time, the value of count becomes the number of 1 when n becomes 0.
        2. Use python function
            n.bit_count()
        """
        cnt=0
        while n:
            n=n&n-1
            cnt+=1
        return cnt