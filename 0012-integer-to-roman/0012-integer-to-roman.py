class Solution:
    def intToRoman(self, num: int) -> str:
        int_map = {1: "I", 4: "IV", 
                      5: "V", 9: "IX", 
                      10: "X", 40: "XL", 
                      50: "L", 90: "XC", 
                      100: "C", 400: "CD", 
                      500: "D", 900: "CM", 
                      1000: "M"}
        result = ""
        
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            while n <= num:
                result += int_map[n]
                num -= n
        return result
        '''
        thounds = num // 1000 
        hundreds = (num % 1000) // 100 
        tens = (num % 100) // 10 
        ones = num % 10 
    
        if thounds:
            result += thounds * "M"
    
        if hundreds:
            if hundreds  == 9:
                result += "CM"
            elif 5 < hundreds < 9:
                result += ("D" + (hundreds - 5) * "C")
            elif hundreds == 5:
                result += "D"
            elif hundreds == 4:
                result += "CD"
            else:
                result += hundreds * "C"
            
        if tens:
            if tens  == 9:
                result += "XC"
            elif 5 < tens < 9:
                result += ("L" + (tens - 5) * "X")
            elif tens == 5:
                result += "L"
            elif tens == 4:
                result += "XL"
            else:
                result += tens * "X"
        
        if ones:
            if ones  == 9:
                result += "IX"
            elif 5 < ones < 9:
                result += ("V" + (ones - 5) * "I")
            elif ones == 5:
                result += "V"
            elif ones == 4:
                result += "IV"
            else:
                result += ones * "I"
        
        
        return result
        '''