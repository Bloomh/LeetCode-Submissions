class Solution:
    def isHappy(self, n: int) -> bool:
        def generateNextN(n):
            newN = 0
            while n:
                newN += (n%10)**2
                n //= 10
            return(newN)
        
        slow, fast = n, generateNextN(n)
        while slow != fast and slow != 1 and fast != 1:
            slow = generateNextN(slow)
            fast = generateNextN(generateNextN(fast))
        return slow == 1 or fast == 1