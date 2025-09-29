class Solution:
    def myPow(self, x: float, n: int) -> float:
        #for small value of n this is working
        #complexity- log(n) which is too slow
        # ans = 1
        # if(n<0):
        #     x=1/x
        #     n=-n
        # while(n>0):
        #     ans=ans*x
        #     n-=1
        # return ans

        #for big value of n Exponentiation by squaring method should be used
        #complexity- log(n)
        ans = 1
        if(n < 0):
            x = 1 / x
            n = -n
        while(n > 0):
            if(n % 2 == 1):
                ans *= x
            x *= x #Squaring the base
            n = n // 2 #Reduce power by half
        return ans

            

        

        