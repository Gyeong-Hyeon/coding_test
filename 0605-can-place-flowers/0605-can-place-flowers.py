class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.insert(0,0)
        flowerbed.append(0)
        i = 1
        while n and (i < len(flowerbed)-1):
            if flowerbed[i-1:i+2] == [0,0,0]:
                flowerbed[i] = 1
                n-=1
            i+=1
        return n <= 0