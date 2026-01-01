class Solution(object):
    def findSubarrays(self, nums):
        n = len(nums)
        s = set()

        for i in range(n-1):
            j = i + 1

            res = nums[i] + nums[j]

            if res in s:
                return True
                
            s.add(res)
        
        return False
        
