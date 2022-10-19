class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1] # keep track of the last open parenthesis – start with -1 which will keep track of the base level (index of where there are zero open parenthese)
        ans = 0
        for i, char in enumerate(s):
            if char == "(": # open another parentheses
                stack.append(i) # add to stack
            elif len(stack)>1: # closing parentheses and stack has more than 1 element
                stack.pop() # close the last open parentheses
                ans = max(ans, i-stack[-1])
            else: # if there is nothing to close so update the 
                stack[0] = i # update index of 0 open parentheses
        return ans