class Solution:
    def isValid(self, s: str) -> bool:
        brackets_check = []
        for i in s:
            if i in "({[":
                brackets_check.append(i)
            else:
                 # list is empty but has closing bracket
                if len(brackets_check) == 0 or \
                (i == ')' and brackets_check[-1] != '(') or \
                (i == ']' and brackets_check[-1] != '[') or \
                (i == '}' and brackets_check[-1] != '{'):
                    return False
                brackets_check.pop()
        return not brackets_check # loop all strings and matches
    
    