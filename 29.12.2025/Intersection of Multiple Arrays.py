class Solution(object):
    def intersection(self, nums):
        ans=[]
        for i in range(0,len(nums[0])):
            s=0
            for j in range(1,len(nums)):
                if nums[0][i]  in nums[j]:
                    s=s+1
            if s==len(nums)-1:
                ans.append(nums[0][i])
        return sorted(ans)
                
