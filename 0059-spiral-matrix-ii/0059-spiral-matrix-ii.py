class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        start_x = 0 # initiate x_val
        start_y = 0 # initiate y_val
        count = 1
        nums = [[0] * n for _ in range(n)] # create n * n matrix
        loop = n // 2 # the totoal number of cycles
        mid = n // 2 # central position
        
        for offset in range(1, loop + 1):
            for i in range(start_y, n - offset): # from left to right [left, right)
                nums[start_y][i] = count
                count += 1
            for i in range(start_x, n - offset): # from top to bottom [top, bottom)
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, start_y, -1): # from right to left [right, left)
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, start_x, -1): # from bottom to top [bottom, top)
                nums[i][start_y] = count
                count += 1
            
            start_x += 1
            start_y += 1
        
        if n % 2 != 0:
            nums[mid][mid] = count
        
        return nums
                
        
        
        
        