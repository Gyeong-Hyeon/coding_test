class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp, prof = float('inf'), 0
        for p in prices:
            if p < bp:
                bp = p
            elif p - bp > prof:
                prof = p - bp
        return prof