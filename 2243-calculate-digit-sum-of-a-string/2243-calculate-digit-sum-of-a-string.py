class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            result = ""

            for i in range(0, len(s), k):
                window = s[i:i+k]

                total = 0
                for digit in window:
                    total += int(digit)

                result += str(total)

            s = result

        return s