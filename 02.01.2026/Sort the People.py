class Solution(object):
    def sortPeople(self, names, heights):
        x = sorted(heights)[::-1]
        a = []
        for i in x:
            a.append(names[heights.index(i)])
        return a
        
