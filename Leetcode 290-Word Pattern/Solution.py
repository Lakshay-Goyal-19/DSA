class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d1={}
        d2={}
        word=s.split()#list
        if(len(word)!=len(pattern)):
            return False
        for i in range(len(word)):
            if(word[i] in d2 and d2[word[i]]!=pattern[i]):
                return False
            if(pattern[i] in d1 and d1[pattern[i]]!=word[i]):
                return False
            d1[pattern[i]]=word[i]
            d2[word[i]]=pattern[i]
        return True

        