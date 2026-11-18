
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        ans = 0
        count = 0

        for i in range(len(s)):

            if s[i] in vowels:
                count += 1

            if i >= k:
                if s[i-k] in vowels:
                    count -= 1

            if i >= k-1:
                ans = max(ans, count)

        return ans
