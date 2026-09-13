class Solution:
    def firstUniqChar(self, s: str) -> int:
        dici = {}

        for ch in s:
            if ch in dici:
                dici[ch] += 1
            else:
                dici[ch] = 1

        for i in range(len(s)):
            if dici[s[i]] == 1:
                return i

        return -1