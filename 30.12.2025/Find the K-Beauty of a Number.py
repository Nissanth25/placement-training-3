class Solution(object):
    def divisorSubstrings(self, num, k):
        l1=str(num)
        l,r=0,k-1
        c=0
        while r<len(l1):
            if int(l1[l:r+1])!=0:
                if num%(int(l1[l:r+1]))==0:
                    c+=1
            r+=1
            l+=1
        return c

        
