class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l1 = s1.split()
        l2 = s2.split()
        d1 = {}
        d2 = {}
        ans = []
        for i in range(len(l1)):
            d1[l1[i]] = d1.get(l1[i],0) + 1
        for i in range(len(l2)):
            d2[l2[i]] = d2.get(l2[i],0) + 1
        for char,num1 in d1.items():
            if char not in d2 and num1 < 2:
                ans.append(char)
        for char,num2 in d2.items():
            if char not in d1 and num2 <2:
                ans.append(char)
        return ans
