class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # i = 0
        # j = len(s)-1
        # while(i < j):
        #     temp = s[i]
        #     s[i] = s[j]
        #     s[j] = temp
        #     i += 1
        #     j -= 1
        def try1(s, start, end):
            if end < start:
                return
            s[start],s[end] = s[end],s[start]
            try1(s,start+1,end-1)
        try1(s,0,len(s)-1)
            


        