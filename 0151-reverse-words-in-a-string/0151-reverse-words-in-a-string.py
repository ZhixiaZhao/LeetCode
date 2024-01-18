class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()
        reverse_string = ""
        
        reverse_string += word_list[-1]
        for i in range(len(word_list) - 2, -1, -1):
            reverse_string += ' '
            reverse_string += word_list[i]
        
        return reverse_string
            
        