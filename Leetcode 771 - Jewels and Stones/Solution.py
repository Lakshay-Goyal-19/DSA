class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d1 = {}
        d2 = {}
        counter = 0
        for i in range(len(jewels)):
            d1[jewels[i]] = d1.get(jewels[i],0) + 1
        for i in range(len(stones)):
            d2[stones[i]] = d2.get(stones[i],0) + 1
        for c,count in d2.items():
            if c in d1: 
                counter += count
        return counter