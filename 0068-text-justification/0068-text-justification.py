class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        currentLine = []
        currentLineLength = 0
    
        for word in words:
            # current line length + length of word that is going to be added in the line 
            # + number of space betwween words.
            if currentLineLength + len(word) + len(currentLine) > maxWidth:
                # total number of spaces that need to be added in the line
                spaces = maxWidth - currentLineLength 
                if len(currentLine) == 1:
                    result.append(currentLine[0] + ' ' * spaces)
                else:
                    # the number of spaces that need to be added in each interval
                    space_between_words = spaces // (len(currentLine) - 1)
                    # extra spaces
                    extra_spaces_between_words = spaces % (len(currentLine) - 1)
                    # or
                    # space_between_words, extra_spaces_between_words = divmod(spaces, 
                    #                                                          len(currentLine) 
                    #                                                          - 1)
                    # add extra spaces firstly
                    for i in range(extra_spaces_between_words):
                        currentLine[i] += ' '
                    result.append((' ' * space_between_words).join(currentLine))
                currentLine = []
                currentLineLength = 0
            currentLine.append(word)
            currentLineLength += len(word)
        result.append(' '.join(currentLine) + ' ' * (maxWidth - currentLineLength 
                                                     - len(currentLine) + 1))
        return result
        