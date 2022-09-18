class Solution:
    def calculate(self, s: str) -> int:
        s.replace(" ","")
        MD = []
        AS = []
        nums = [[]]
        for i in range(len(s)):
            if s[i] == '/' or s[i] == '*':
                MD.append((len(nums)-len(MD)-1,s[i]))
                nums.append([])
            elif s[i] == '-' or s[i] == '+':
                AS.append((len(nums)-len(MD)-len(AS)-1,s[i]))
                nums.append([])
            else:
                nums[-1].append(s[i])
        nums = [int(''.join(i)) for i in nums]
        for ind, op in MD:
            nxt = nums.pop(ind+1)
            if op == '*':
                nums[ind] = nums[ind]*nxt
            else:
                nums[ind] = nums[ind]//nxt
        for ind, op in AS:
            nxt = nums.pop(ind+1)
            if op == '+':
                nums[ind] = nums[ind]+nxt
            else:
                nums[ind] = nums[ind]-nxt
        return nums[0]
        