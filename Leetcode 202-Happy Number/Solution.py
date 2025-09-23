class Solution:
    def s(self,n1):
        sum=0
        while(n1>0):
            a=n1%10
            a=a*a
            sum+=a
            n1=n1//10
        return sum
    def isHappy(self, n: int) -> bool:
        slow=n
        fast=n
        while True:
            slow=self.s(slow)
            fast=self.s(self.s(fast))
            if fast==1:
                return True
            if slow==fast:
                return False


    



        