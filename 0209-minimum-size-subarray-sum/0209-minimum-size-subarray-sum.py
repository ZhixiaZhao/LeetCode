class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        else:
            total = 0
            min_len = len(nums)
            left = 0
            for idx, val in enumerate(nums):
                total += val
                while total >= target:
                    min_len = min(min_len, idx - left + 1)
                    total -= nums[left]
                    left += 1
            return min_len
        # from left to right, we add value one by one， 
        # once the sum is greater than target, fix right pointer, and move left pointer.
        # if the target is less than target, move right pointer.
        # if the target is still greater than target, move left pointer to find the minimum
        # size.
        