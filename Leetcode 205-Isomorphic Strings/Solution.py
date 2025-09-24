class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        d1={}
        d2={}
        for i in range(len(s)):
            if(d1.get(s[i]) not in d2 and d2.get(t[i]) not in d1):#new mapping
                d1[s[i]]=t[i]
                d2[t[i]]=s[i]
            else:
                if(s[i]!=d2.get(t[i]) and t[i]!=d1.get(s[i])):
                    return False
        return True


        
        
        