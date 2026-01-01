class Solution(object):
    def smallestEvenMultiple(self, n):
        return n << (n & 1)
