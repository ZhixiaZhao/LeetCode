class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle in haystack:
            return -1
        else:
            haystack_len = len(haystack)
            needle_len = len(needle)
            for i in range(0, haystack_len - needle_len + 1):
                if haystack[i: i + needle_len] == needle:
                    return i
        