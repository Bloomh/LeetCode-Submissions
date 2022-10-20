class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        lettersToValues = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        for letter, value in lettersToValues.items():
            while num >= value:
                num -= value
                ans += letter
        return ans
                