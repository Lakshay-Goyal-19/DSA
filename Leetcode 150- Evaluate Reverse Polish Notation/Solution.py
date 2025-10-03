import operator 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+": operator.add,
                "-": operator.sub,
                "*": operator.mul,
            }
        for i in range(len(tokens)):
            if(tokens[i] != '+' and tokens[i] != '-' and tokens[i] != '*' and tokens[i] != '/' ):
                stack.append(int(tokens[i]))
            else:
                top = stack.pop()
                top2 = stack.pop()
                if(tokens[i] == '/'):
                    ans = int(top2 / top)
                else:
                    ans = ops[tokens[i]](top2 , top)
                stack.append(ans)
        return stack[-1]
        