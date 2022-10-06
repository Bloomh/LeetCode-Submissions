class Solution:
    def sum(self, num1: int, num2: int) -> int:
        if not (num1 and num2): #base case – one of the integers is zero
            return num1 or num2 #return the one that exists
        elif num1 < 0 and num2 < 0: #both negative numbers
            return -self.sum(-num1,-num2) #fix to be positive
        if num2 > num1:
            num1, num2 = num2, num1 #make sure num1 is the bigger integer
        return 1 + self.sum(num1-1,num2) #recursive call
        