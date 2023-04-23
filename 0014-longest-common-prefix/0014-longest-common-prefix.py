class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        # if len(strs) == 1:
        #     return strs[0]
        # common_prefix = ""
        for i in range(len(strs[0])):
            common_prefix = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != common_prefix:
                    return strs[0][0:i]
        return strs[0]