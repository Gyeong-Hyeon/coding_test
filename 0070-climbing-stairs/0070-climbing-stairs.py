class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Combination(n) = Combination(n-1) + Combination(n-2)        
        """
        comb = [0,1,2,3,5,8,13]
        if n < len(comb):
            return comb[n]
        else:
            while len(comb)-1 < n:
                comb.append(comb[-2] + comb[-1])
            return comb[-1]