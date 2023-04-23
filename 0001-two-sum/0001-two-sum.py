class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Using hashmap to solve
        preMap = {} #{value: index}
        for idx, num in enumerate(nums):
            remaining = target - num
            if remaining in preMap:
                return [preMap[remaining], idx]
            else:
                preMap[num] = idx
