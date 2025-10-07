class Solution:
    def addDigits(self, num: int) -> int:
            if num == 0:
                return 0    
            sum = 0
            while(num != 0):
                a = num % 10
                sum += a
                num = num // 10
            if sum >= 10:
                return self.addDigits(sum)
            else:
                return sum
       
        