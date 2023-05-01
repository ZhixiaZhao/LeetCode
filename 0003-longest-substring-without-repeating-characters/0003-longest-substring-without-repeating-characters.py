class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        if len(s) <= 1:
            return len(s)
        else:
            for i in range(len(s)):
                str_array = []
                for j in range(i, len(s)):
                    if s[j] not in str_array:
                        str_array.append(s[j])
                    else:
                        break
                max_len = max(max_len, len(str_array))
        return max_len
        