class Solution(object):
    def percentageLetter(self, s, letter):
        char1_count = {}
        
        for char in s:
            if char in char1_count:
                char1_count[char] += 1
            else:
                char1_count[char] = 1
        count1 = char1_count.get(letter, 0)
        percentage = (count1 * 100) // len(s)
        return percentage


        
