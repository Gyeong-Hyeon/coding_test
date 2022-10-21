class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def change(r,c):
            if r < 0 or c < 0 or r == len(image) or c == len(image[0]) or image[r][c] != s:
                return 0
            image[r][c] = color
            return change(r-1, c), change(r+1,c), change(r,c-1), change(r,c+1)        
        s = image[sr][sc]
        if s != color:
            change(sr,sc)
        return image
