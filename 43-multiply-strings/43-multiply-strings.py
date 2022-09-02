class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        n1 = len(num1)-1
        n2 = len(num2)-1
        for i in range(len(num1)):
            for j in range(len(num2)):
                ans += int(num1[i])*int(num2[j])*(10**(n1-i+n2-j))
        return str(ans)
            
            