class Solution:
    def mySqrt(self, x: int) -> int:
        # return int(x**0.5)
        if(x==0):
            return 0
        start=1
        end=x
        while(start<=end):
            middle=(end+start)//2
            if(middle*middle==x):
                return middle
            if(middle*middle<x):
                start=middle+1
            else:
                end=middle-1
        return end
    
        