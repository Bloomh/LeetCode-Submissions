class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        reverse = binary[::-1]
        fixed = reverse + "0"*(32-len(reverse))
        return int(fixed, 2)