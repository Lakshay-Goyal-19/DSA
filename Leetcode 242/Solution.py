class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=1
            else:
                d[s[i]]+=1
        for i in range(len(t)):
            if t[i] not in d:
                return False
            else:
                d[s[i]]-=1
        return True
       