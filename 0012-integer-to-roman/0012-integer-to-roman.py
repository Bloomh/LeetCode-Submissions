class Solution:
    def intToRoman(self, num: int) -> str:
        ans = []
        while num >= 900:
            num -= 1000
            ans += ['M']
        if num < 0:
            num += 100
            ans.insert(-1,'C')
        while num >= 400:
            num -= 500
            ans += ['D']
        if num < 0:
            num += 100
            ans.insert(-1,'C')
        while num >= 90:
            num -= 100
            ans += ['C']
        if num < 0:
            num += 10
            ans.insert(-1,'X')
        while num >= 40:
            num -= 50
            ans += ['L']
        if num < 0:
            num += 10
            ans.insert(-1,'X')
        while num >= 9:
            num -= 10
            ans += ['X']
        if num < 0:
            num += 1
            ans.insert(-1,'I')
        while num >= 4:
            num -= 5
            ans += ['V']
        if num < 0:
            num += 1
            ans.insert(-1,'I')
        ans += ['I'] * num
        return ''.join(ans)
        
        