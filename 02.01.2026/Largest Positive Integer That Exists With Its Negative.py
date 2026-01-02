class Solution(object):
    def findMaxK(self, nums):
        k = -1
        nums_set = set(nums)
        for n in nums:
            if n > 0:
                if n > k and -n in nums_set:
                    k = n


        return k
