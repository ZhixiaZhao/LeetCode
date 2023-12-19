class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        length = len(citations)
        h = []
        for i, num in enumerate(citations):
            # h = max(h, min(num, length - i))
            if num >= length - i:
                return length - i
        return 0
'''
There are three conditions:
1). If the array contains only one element and it is greater than zero, the h-index is 1.
2). If the smallest value in the sorted array is greater than or equal to the length of the array, the h-index is equal to the length of array.
3). 


 Otherwise, the array is traversed, and for each index i, the value at that index is compared to i+1. If the value is less than i+1, i is returned as the h-index. If none of the conditions are met, the h-index is 0.
'''