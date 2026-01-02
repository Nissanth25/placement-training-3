class Solution(object):
    def averageValue(self, nums):
        store = [v for v in nums if v % 6 == 0]
        return sum(store) // len(store) if len(store) != 0 else 0
