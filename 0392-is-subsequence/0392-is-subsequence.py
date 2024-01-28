class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        Two pointers (i and j), i traverse s, j traverse t.
        
        '''
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
        