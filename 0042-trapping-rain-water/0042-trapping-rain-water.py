class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeftHeight = []
        maxRightHeight = []
        minLeftRight = []
        result = 0
        n = len(height)
    
        maxLeft = height[0]
        for i in range(n):
            maxLeftHeight.append(maxLeft)
            if maxLeft < height[i]:
                maxLeft = height[i]
            
        maxRight = height[-1]
        for i in range(n - 1, -1, -1):
            maxRightHeight.append(maxRight)
            if maxRight < height[i]:
                maxRight = height[i]
        maxRightHeight = list(reversed(maxRightHeight))
    
        for i in range(n):
            h = min(maxLeftHeight[i], maxRightHeight[i]) - height[i]
            if h > 0:
                result += h
        
        return result    