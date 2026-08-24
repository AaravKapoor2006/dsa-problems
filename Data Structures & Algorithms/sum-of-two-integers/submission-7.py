class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b & mask:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        # mask a to 32 bits
        a = a & mask

        # if sign bit (bit 31) is set → negative number
        if a >> 31:
            return ~(a ^ mask)
        return a