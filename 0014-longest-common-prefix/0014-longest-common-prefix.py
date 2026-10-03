class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for char in zip(*strs):
            if len(set(char)) == 1:
                prefix += char[0]
            else:
                break
        return prefix