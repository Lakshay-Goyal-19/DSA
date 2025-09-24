class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1={}
        d2={}
        for i in range(len(magazine)):
            d1[magazine[i]]=d1.get(magazine[i],0)+1
        for i in range(len(ransomNote)):
            d2[ransomNote[i]]=d2.get(ransomNote[i],0)+1
        for char,count in d2.items():
            if count>d1.get(char,0):
                return False
        return True

        
        
        