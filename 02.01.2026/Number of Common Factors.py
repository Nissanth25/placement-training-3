class Solution(object):
    def commonFactors(self, a, b):
        x = min(a,b)
        y = 0
        for i in range(1,x+1):
                if(a%i==0 and b%i==0):
                        y += 1
        return y
