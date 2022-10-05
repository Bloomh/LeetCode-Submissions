class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [] #stack will keep track of closing brackets we need
        for char in s: #iterate over all characters
            #first we will check to see if char is an opening bracket and if it is, then we add the corresponding closing bracket to stack
            if char == '(': 
                stack.append(')')
            elif char == '[':
                stack.append(']')
            elif char == '{':
                stack.append('}')
            elif len(stack) == 0 or not char == stack.pop():
                #if stack is empty or the last bracket is not the one we expect, then the parentheses are invalid
                return False
        return len(stack) == 0 #if there are any closing brackets we still expected, then the parentehses are invalid