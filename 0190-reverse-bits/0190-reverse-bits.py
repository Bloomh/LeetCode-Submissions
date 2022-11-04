class Solution:
    def reverseBits(self, n: int) -> int:
        # start with the answer being zero (like an empty binary string)
        answer = 0
        # we need to get all 32 bits
        for _ in range(32):
            # get the last bit of n by getting the remainder mod 2
            last_bit_of_n = n % 2
            # divide n by two to effectively move the digits to the right
            n = n // 2
            # move the digits in our answer to the left by multiplying by two
            answer = answer * 2
            # add the last bit of n to our answer
            answer = answer + last_bit_of_n
        # return the answer
        return answer