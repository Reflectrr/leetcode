class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        sign = (
            1
            if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
            else -1
        )
        dividendAbs, divisorAbs = abs(dividend), abs(divisor)
        while dividendAbs >= divisorAbs:
            tempDivisor, factors = divisorAbs, 1
            while dividendAbs >= tempDivisor:
                tempDivisor <<= 1
                factors <<= 1
            factors >>= 1
            tempDivisor >>= 1
            dividendAbs -= tempDivisor
            res += factors
        res *= sign
        return min(max(res, -(2**31)), 2**31 - 1)
