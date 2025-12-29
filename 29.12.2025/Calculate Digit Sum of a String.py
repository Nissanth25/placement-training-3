class Solution(object):
    def digitSum(self,s,k):
        n=len(s)
        while n>k:
            s2=""
            k1=k
            for i in range(0,n,k):
                s1=s[i:k1]
                k1=k1+k
                sum1=0
                for j in s1:
                    sum1=sum1+int(j)
                s2=s2+str(sum1)
            s=s2
            n=len(s)
        return s
