class Solution(object):
    def oddString(self, words):
        diff0 = []
        for j in range(1, len(words[0])):
            diff0.append(ord(words[0][j]) - ord(words[0][j-1]))
        diff1 = []
        same = True
        for j in range(1, len(words[1])):
            diff1.append(ord(words[1][j]) - ord(words[1][j-1]))
            if diff0[j-1] != diff1[-1]: same = False
        if same:
            for i in range(2, len(words)): 
                for j in range(1, len(words[i])):
                    if diff0[j-1] != ord(words[i][j]) - ord(words[i][j-1]): return words[i]
        else:
            diff2 = []
            for j in range(1, len(words[2])):
                diff = ord(words[2][j]) - ord(words[2][j-1])
                if diff != diff0[j-1]: return words[0]
                elif diff != diff1[j-1]: return words[1]
