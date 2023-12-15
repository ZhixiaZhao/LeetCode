class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # DO not nums = list(dict.fromkeys(nums)) because the id of new list has been changed.
        # [:] makes a shallow copy of the list
        # shallow copy VS. deep copy
        '''
        nums[:] = list(set(nums))
        return len(nums)
        '''
        
        k = 0
        for i in range(1, len(nums)):
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]
        return k + 1
        