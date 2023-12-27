class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        
        prefix = 1 # from the first place to the last place
        for i in range(len(nums)):
            ans[i] = prefix
            prefix = prefix * nums[i]
            
        postfix = 1 # from the last place to the first place
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = ans[i] * postfix
            postfix = postfix * nums[i]
            
        return ans