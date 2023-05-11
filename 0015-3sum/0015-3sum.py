class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort the list
        result = []
        for i in range(len(nums) - 2):
            # because this is a sorted list, if the first one is larger than 0, the remaining two numbers will be larger than 0
            if nums[i] > 0:
                return result 
            # skip same numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]: # watch out left - 1
                        left += 1
                    while left < right and nums[right] == nums[right + 1]: # watch out right + 1
                        right -= 1
                
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                else:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return result
                
        