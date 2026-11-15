class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7

        odd = 0
        even = 1
        prefix = 0
        count = 0

        for num in arr:
            prefix += num

            if prefix % 2 == 0:
                count += odd
                even += 1
            else:
                count += even
                odd += 1

        return count % MOD