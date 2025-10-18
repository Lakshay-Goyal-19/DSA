class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ans = ""
        for char in s:
            if char == '(':
                if len(stack) > 0:
                    ans += '('
                stack.append('(')
            else:
                stack.pop()
                if(len(stack) > 0):
                    ans += ')'
        return ans
        