class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        length = len(citations)
        h = []
        for i, num in enumerate(citations):
            if num >= length - i:
                return length - i
        return 0