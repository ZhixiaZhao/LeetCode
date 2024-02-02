class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        countT, window = {}, {}
        for i in t:
            countT[i] = 1 + countT.get(i, 0)
#         dictionary.get(keyname, value)
#         keyname: Required. The keyname of the item you want to return the value from
#         value: Optional. A value to return if the specified key does not exist.Default value None
        have, need = 0, len(countT)
        res = [-1, -1]
        resLen = float("infinity")
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)
            if c in countT and countT[c] == window[c]:
                have += 1
            while have == need:
                if right - left + 1 < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        left, right = res
        if resLen != float("infinity"): 
            return s[left:right + 1]
        else:
            return ""
            
            
        