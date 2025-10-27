class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        method = [0]*len(bank)
        ans = 0
        for i in range(len(bank)):
            for j in range(len(bank[i])):
                if(bank[i][j] == '1'):
                    method[i] += 1
        prev = 0
        for i in method:
            if i==0:
                continue
            ans += prev * i
            prev = i 
        return ans