class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_num = sorted(nums1 + nums2)
        if len(merged_num) % 2 == 0:
            idx = int(len(merged_num) / 2)
            median = (merged_num[idx-1] + merged_num[idx])/2
        else:
            idx = len(merged_num) // 2
            median = merged_num[idx]
        return median