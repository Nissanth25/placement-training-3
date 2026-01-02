class Solution(object):
    def equalFrequency(self, word):
        counting=Counter(word)
        for i in word:
            counting[i]-=1
            newlist=[]
            for j in counting.values():
                if j:
                    newlist.append(j)
            if len(set(newlist))==1:
                return True
            counting[i]+=1
        return False
        
