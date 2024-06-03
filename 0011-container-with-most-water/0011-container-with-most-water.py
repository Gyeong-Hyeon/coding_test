class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, max_area = 0, len(height)-1, 0

        while left < right:
            area = min(height[left], height[right])*(right-left)
            max_area = max(max_area, area)
            
            if height[left] > height[right]:
                right-=1
            elif height[left] < height[right]:
                left+=1
            else:
                if height[left+1] >= height[right-1]:
                    right-=1
                else:
                    left+=1
        
        return max_area
