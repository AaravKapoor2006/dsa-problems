class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        og = abs(x)
        res = 0

        while og > 0:
            digit = og % 10
            og = og // 10
            res = res * 10 + digit

        if res < -2**31 or res > 2**31 - 1:
            return 0

        return sign * res