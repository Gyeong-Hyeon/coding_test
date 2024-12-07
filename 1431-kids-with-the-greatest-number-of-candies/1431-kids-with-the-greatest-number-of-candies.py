class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy, ans = max(candies), [False]*len(candies)
        for i, candy in enumerate(candies):
            if candy + extraCandies < max_candy:
                ans[i] = False
            else:
                ans[i] = True
        return ans