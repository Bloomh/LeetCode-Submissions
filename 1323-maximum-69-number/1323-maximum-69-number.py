class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        for i, char in enumerate(num):
            if char == '6':
                return int(num[:i] + '9' + num[i+1:])
        return int(num)