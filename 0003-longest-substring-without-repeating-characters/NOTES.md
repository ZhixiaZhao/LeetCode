use slide window to solve this problem:
​
```
class Solution:
def lengthOfLongestSubstring(self, s: str) -> int:
seen = {}
l = 0
output = 0
for r in range(len(s)):
"""
If s[r] not in seen, we can keep increasing the window size by moving right pointer
"""
if s[r] not in seen:
output = max(output,r-l+1)
"""
There are two cases if s[r] in seen:
case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
case2: s[r] is not inside the current window, we can keep increase the window
"""
else:
if seen[s[r]] < l:
output = max(output,r-l+1)
else:
l = seen[s[r]] + 1
seen[s[r]] = r
return output
```
​
or:
```
class Solution:
def lengthOfLongestSubstring(self, s: str) -> int:
char_set = set()
max_len, start = 0, 0
for i, c in enumerate(s):
while c in char_set:
char_set.remove(s[start])
start += 1
char_set.add(c)
max_len = max(max_len, i - start + 1)
return max_len
```