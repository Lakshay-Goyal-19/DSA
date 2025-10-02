class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = path.split('/')
        n = len(stack)
        ans = "" 
        res = []
        for i in range(n):
            if(stack[i] == '' or stack[i] == '.'):
                continue
            if(stack[i] == '..'):
                if res:
                    res.pop()
            else:
                res.append(stack[i])
        ans = "/" + "/".join(res)
        return ans
            

            
                        
                