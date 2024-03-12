class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
        '''
        
        # Two Pointers
        fast = 0 # find the element in the new arreay
        slow = 0 # update the position in the new array
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[slow] = nums[i]
                slow += 1
            fast += 1
        return slow
        