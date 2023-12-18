class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach_idx = 0
        for i, num in enumerate(nums):
            if i > reach_idx:
                return False
            reach_idx = max(reach_idx, i + num)
        return True
    
# greedy algorithm
            
        