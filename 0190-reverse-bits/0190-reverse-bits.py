class Solution:
    def reverseBits(self, n: int) -> int:
        """
        1. Pythonic
            The function bin(n) revmoves all 0 at left, changes n to string and add '0b' at the front.
            So, reverse bin(n)[2:] and add 32-len(bin(n)[2:]) of zeros to the left. (because n was 32 bits)
        """
        n = bin(n)[2:]
        n = '0'*( 32-len(n) ) + n
        return int( n[::-1] ,2)