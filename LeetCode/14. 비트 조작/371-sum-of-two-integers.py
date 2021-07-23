# https://leetcode.com/problems/sum-of-two-integers/

# Given two integers a and b, return the sum of the two integers without using the operators + and -.


class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0b11111111111
        INT_MAX = 0b01111111111
        a_bin = bin(a & MASK)[2:].zfill(12)
        b_bin = bin(b & MASK)[2:].zfill(12)
        result = ''
        Cin = 0

        for i in range(12):
            A, B = int(a_bin[11 - i]), int(b_bin[11 - i])
            A_xor_B = A ^ B
            S = A_xor_B ^ Cin
            Cin = (A & B) | (Cin & A_xor_B)
            result += str(S)

        result = int(result[::-1], 2) & MASK

        if result > INT_MAX:
            result = ~(result ^ MASK)

        return result
