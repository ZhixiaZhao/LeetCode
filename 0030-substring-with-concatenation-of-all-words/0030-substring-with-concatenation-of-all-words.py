class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words.sort()
        words_len = len(words)
        word_len = len(words[0])
        slide_len = words_len * word_len
        ans = []
        for i in range(0, len(s) - slide_len + 1):
            s_sub = s[i: i + slide_len]
            temp_words = []
            for j in range(0, len(s_sub), word_len):
                word = s_sub[j: j + word_len]
                temp_words.append(word)
            temp_words.sort()
            if temp_words == words:
                ans.append(i)
        return ans
        