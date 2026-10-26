from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c in '([{':
                stack.append(c)
            elif c in '}])':
                if not stack:
                    return False
                else:
                    p = stack.pop()
                    if c == '}' and p != '{':
                        return False
                    elif c == ']' and p != '[':
                        return False
                    elif c == ')' and p != '(':
                        return False
        if not stack:
            return True
        else:
            return False
        