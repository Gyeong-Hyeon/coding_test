class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        1. if n <= 0 not power of 2, 1 and 2 is power of 2
        2. from 3, bit(n) starts with 1 and the other digits are 0 when n is a power of 2.
        """
        if n <= 0:
            return False
        if n <= 2:
            return True
        bit = bin(n)[2:]
        if bit[0] == '1' and set(bit[1:]) == {'0'}: return True
        else: return False