class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True
        flowerbed.insert(0,0)
        flowerbed.append(0)
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1:i+2] == [0,0,0]:
                flowerbed[i] = 1
                n-=1
            if n == 0:
                return True
        return n == 0