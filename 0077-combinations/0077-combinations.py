class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Pascal's Identity - nCk = n-1Ck + n-1Ck-1
        So nCr will be n-1Ck + adding n to each combination of n-1Ck-1.
        Therefore, we can devide this problem in 4small problems.
        1. When k == 0: Retuns an empty list since the number of elements in the combination is 0.
        2. When k == 1: Each element in the list is a combination, the number of combination is n.
        3. When n == k: 1~n will be one combination. The number of combination is 1.
        4. Else, call n-1Ck and n-1Ck-1 appended n to the each combination
        """
        if k == 0:
            return []
        if k == 1:
            return [[i] for i in range(1, n+1)]
        if n == k:
            return [[i for i in range(1, n+1)]]
        ans = self.combine(n-1,k-1)
        ans = [comb + [n] for comb in ans]
        ans.extend(self.combine(n-1,k))
        return ans