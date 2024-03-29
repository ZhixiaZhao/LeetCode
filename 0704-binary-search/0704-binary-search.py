class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        if target not in nums:
            return -1
        else:
            return nums.index(target)
        
        '''
        
        # Binary search 
        
        # [left, right]
#         left = 0
#         right = len(nums) - 1
        
#         while left <= right:
#             middle = (left + right) // 2
            
#             if nums[middle] > target:
#                 right = middle - 1
#             elif nums[middle] < target:
#                 left = middle + 1
#             else:
#                 return middle
#         return -1
    
        # [left, right)
        left = 0
        right = len(nums)
        
        while left < right:
            middle = (left + right) // 2
            
            if nums[middle] > target:
                right = middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1
        
        
            
        
        