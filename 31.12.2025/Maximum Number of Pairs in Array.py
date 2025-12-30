class Solution(object):
    def numberOfPairs(self, nums):
        hashT = {}
        for n in nums:
            if n not in hashT: hashT[n] = 1
            else: hashT[n] += 1
        pairs, rem = 0, 0
        for n in hashT:
            pairs += (hashT[n] // 2)
            rem += (hashT[n] % 2)
        return [pairs, rem]
