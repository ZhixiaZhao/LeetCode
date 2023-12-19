class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        length = len(citations)
        h = 0
        for i, num in enumerate(citations):
            h = max(h, min(num, length - i))             
        return h
                
        