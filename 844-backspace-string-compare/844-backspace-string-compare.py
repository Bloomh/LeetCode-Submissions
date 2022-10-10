class Solution(object):
    def backspaceCompare(self, s, t):
        def textEditor(string):
            stack = []
            for char in string:
                if char != "#":
                    stack.append(char)
                elif stack:
                    stack.pop()
            return stack
        
        return textEditor(s) == textEditor(t)