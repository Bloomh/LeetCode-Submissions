class Solution:
    def reverseBits(self, n: int) -> int:
        # our result string will start empty
        result = ""
        # turn n into a binary string
        binary = bin(n)[2:]
        # add zeroes to the beginning of the binary string to make it 32 bits
        binary = "0"*(32-len(binary)) + binary
        # now we will use a for loop to iterate over the binary string backwards
        # i will start at 31 and end up at 0, going backwards
        for i in range(31,-1,-1): 
            # add the last element of binary to result
            result += binary[i]
        # convert the resulting string to an integer
        return int(result, 2)