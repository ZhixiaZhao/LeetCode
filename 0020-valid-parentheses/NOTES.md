also can use dictionary to determin if the string is valid
```
dict = {"(": ")", "{": "}", "[", "]"}
stack = []
for i in s:
if i in '([{':
stack.append(i)
else:
if not stack:
return False
if stack[-1] != opening[br]:
return False
stack.pop()
​
return not stack
```