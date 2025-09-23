class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs=sorted(strs)
        ans=""
        first=strs[0]
        last=strs[-1]
        if(len(strs)==0):
            return ans
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            else:
                ans+=first[i]
        return ans

        