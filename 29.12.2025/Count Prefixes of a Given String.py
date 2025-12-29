class Solution(object):
        def countPrefixes(self, words, s):
            return sum(map(s.startswith, words))

