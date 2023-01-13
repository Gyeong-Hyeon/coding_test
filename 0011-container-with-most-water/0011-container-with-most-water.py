class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end, max_area = 0, len(height)-1, 0
        
        while start < end:
            w = end-start
            h = min(height[start], height[end])
            
            if w*h > max_area:
                max_area = w*h
            
            if height[start] > height[end]:
                end-=1
            elif height[end] > height[start]:
                start+=1
            else:
                if height[end-1] >= height[start+1]:
                    end-=1
                else:
                    start+=1
        return max_area