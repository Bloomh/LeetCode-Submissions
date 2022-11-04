class Solution:
    def reverseBits(self, n: int) -> int:
        # start with the answer being 
        answer = 0
        # we need to get all 32 bits
        for _ in range(32):
            # get the last bit of n by using n & 1
            last_bit_of_n = n & 1
            # shift all the bits in our answer to the left by 1 spot
            answer = answer << 1
            # add the last bit of n to the end of our answer using answer XOR last_bit_of_n
            answer = answer ^ last_bit_of_n
            # shift all the bits in n to the right by 1 spot
            n = n >> 1
        return answer
            