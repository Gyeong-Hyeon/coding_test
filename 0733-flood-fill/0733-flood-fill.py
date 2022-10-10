class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        if start != color:
            image[sr][sc] = color
            v = [(sr,sc)]
            while v:
                r,c = v[0][0], v[0][1]
                v.remove((r,c))
                if r+1 < len(image):
                    if image[r+1][c] == start:
                        image[r+1][c] = color
                        v.append((r+1,c))
                if r-1 > -1:
                    if image[r-1][c] == start:
                        image[r-1][c] = color
                        v.append((r-1,c))
                if c+1 < len(image[0]):
                    if image[r][c+1] == start:
                        image[r][c+1] = color
                        v.append((r,c+1))
                if c-1 > -1:
                    if image[r][c-1] == start:
                        image[r][c-1] = color
                        v.append((r,c-1))
        return image