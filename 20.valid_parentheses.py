class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paranMap = {')': '(', '}':'{', ']':'['}

        for char in s:
            if char in ['(','[','{']:
                stack.append(char)
            elif char in paranMap:
                if stack and stack[-1] == paranMap[char]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
