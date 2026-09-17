class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        ans = n + 1
        w_s = 0
        left = 0

        dp = [n] * (n + 1)

        for right in range(n):
            w_s += arr[right]

            while w_s > target:
                w_s -= arr[left]
                left += 1

            dp[right + 1] = dp[right]

            if w_s == target:
                length = right - left + 1

                ans = min(ans, length + dp[left])

                dp[right + 1] = min(dp[right], length)

        return -1 if ans == n + 1 else ans