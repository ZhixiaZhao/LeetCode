class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        # Two pointers
        left = 0
        right = len(height) - 1
        
        maxLeft = height[left]
        maxRight = height[right]
        result = 0
        
        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                result += (maxLeft - height[left])
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                result += (maxRight - height[right])
        return result
        
        
        
        
        
        '''
        # Two traverses
        # original                 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1
        # max left                 0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3
        # max right                3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 1
        # min(max left, max right) 0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1
        
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
        '''
        