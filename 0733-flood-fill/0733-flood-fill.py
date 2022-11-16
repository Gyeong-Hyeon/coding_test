class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        1. set variable num to current image[sr][sc]'s value
        2. Define a function "change_color" doing:
            - parameter: row_idx, col_idx
            - Return False if one of the following case is true:
                - row_idx < 0
                - row_idx >= len(image)
                - col_idx < 0
                - col_idx >= len(image[0])
                - image[row_idx][col_idx] != num
            - Else, change image[row_idx][col_idx]'s value to num
            - call function change_color(row_idx-1, col_idx) change_color(row_idx+1, col_idx) change_color(row_idx, col_idx-1) change_color(row_idx, col_idx-1)
        3. if num != color: change_color(sr,sc)
        """
        org = image[sr][sc]
        if org == color:
            return image
        def change_color(r,c):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != org:
                return False
            image[r][c] = color
            return change_color(r-1,c), change_color(r+1,c), change_color(r,c-1), change_color(r,c+1)
        change_color(sr,sc)
        return image
