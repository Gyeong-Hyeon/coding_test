class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        - Basic
        1. if n <= 0 not power of 2, 1 and 2 is power of 2
        2. from 3, bit(n) starts with 1 and the other digits are 0 when n is a power of 2.
        
        - Using bit manipulation
        1. When n is a power of 2, n is 1000...0 and n-1 is 111...1, len(bit(n))-len(bit(n-1)) is 1
            Therefore, when we do n&n-1, it will always return False when n is a power of 2 because n&n-1 is 0
            On the other hand, when n is not a power of 2, len(bit(n)) = len(bit(n-1)) so n&n-1 > 0 == True.
            Also, n == True when n != 0.
        2. When n is 0, n == False.
        3. In conculsion, we can return n and not (n&n-1). It will be True when n is a power of 2, False when n is not a power of 2.
        """
        return n and not (n&n-1)