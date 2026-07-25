class Solution:
    def characterReplacement(self, s: str, k: int):
        freq = {}
        l = 0
        maxFreq = 0
        ans = 0

        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1
            if freq[s[r]] > maxFreq:
                maxFreq = freq[s[r]]
            while (r - l + 1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans