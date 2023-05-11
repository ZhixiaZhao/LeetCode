class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        for i in range(len(s)):
            odd = self.expand(s, i, i)
            even = self.expand(s, i, i + 1)
            res = max(res, odd, even, key = len)
        return res
        
    
    def expand(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
            
        return s[i+1 : j]
        