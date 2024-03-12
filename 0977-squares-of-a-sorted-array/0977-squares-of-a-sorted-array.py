class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # initial thought: square then sort
        # for i in range(len(nums)):
        #     nums[i] = nums[i] * nums[i]
        # nums.sort()
        # return nums
    
        # Two Pointers
        # the array is sorted in non-decreasing, so the maximum values should at the right or left of the original array
        i = 0
        j = len(nums) - 1
        k = len(nums) - 1 # the index in the new array
        result = [0] * len(nums)
        
        while i <= j:  # not i < j
            if nums[i] ** 2 < nums[j] ** 2:
                result[k] = nums[j] ** 2
                j -= 1
            else:
                result[k] = nums[i] ** 2
                i += 1
            k -= 1
        return result
    
    
        