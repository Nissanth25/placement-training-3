class Solution(object):
    def minimumOperations(self, A):
        return len(set(A) - {0})
        
