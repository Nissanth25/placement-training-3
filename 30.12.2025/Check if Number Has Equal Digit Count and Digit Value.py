class Solution(object):
    def digitCount(self, num):
        list = [0] * 10
        for n in num:
            list[int(n)] += 1
        
        for i in range(0, len(num)):
            if list[i] == int(num[i]):
                continue
            else:
                return False
        return True


        
