class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in s:
            if not i.isalnum():
                s = s.replace(i, "")
        s = s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        
        