from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs',
                '8': 'tuv', '9': 'wxyz'}
        '''
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return list(phone[digits])
        else:
            result = []
            chars = [phone[digit] for digit in digits]
            combinations = product(*chars)
            for i in combinations:
                combination = "".join(i)
                result.append(combination)
            return result
            '''
        if len(digits) == 0:
            return []
        else:
            result = []
            chars = [phone[digit] for digit in digits]
            combinations = product(*chars)
            for i in combinations:
                combination = "".join(i)
                result.append(combination)
            return result
            
        
        