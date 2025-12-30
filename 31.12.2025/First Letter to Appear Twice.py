class Solution(object):
    def repeatedCharacter(self, s):
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    return s[i]
                for k in range(i+1,j):
                    if s[k]==s[j]:
                        return s[k]
                
        else:
            return 
