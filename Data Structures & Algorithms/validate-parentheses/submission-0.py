class Solution:
    def isValid(self, s: str) -> bool:
        dc = {')': '(', '}':'{', ']':'['}
        stack = []

        for c in s:
            if c in dc:
                if stack and stack[-1] == dc[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False



        