class Solution:
    def f(self,n):
        ans = []
        for i in range(1,n+1):
            if(n % i == 0):
                ans.append(i)
        return ans
    def repeatedSubstringPattern(self, s: str) -> bool:
        fac = self.f(len(s))
        for div in fac:
            if div == len(s):
                continue  
            parts = [s[i:i+div] for i in range(0, len(s), div)]
            if all(part == parts[0] for part in parts):
                return True
        return False
        