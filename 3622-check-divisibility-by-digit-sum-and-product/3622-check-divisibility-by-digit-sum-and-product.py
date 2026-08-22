class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original = n

        n_sum = 0
        n_product = 1

        while n > 0:
            digit = n % 10
            n //= 10
            n_sum += digit
            n_product *= digit

        return original % (n_sum + n_product) == 0