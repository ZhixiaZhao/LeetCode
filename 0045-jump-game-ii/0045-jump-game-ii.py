class Solution:
    def jump(self, nums: List[int]) -> int:
        current = 0 # The farthest distance at current position
        count = 0 # count the minimum number of jumps
        position = 0
        n = len(nums)
        while current < n - 1:
            count += 1
            previous = current
            
            while position <= previous:
                current = max(current, position + nums[position])
                position += 1
        return count
    

        