class Solution(object):
    def rearrangeCharacters(self, s, target):
        check = len(s)

        for i in target:
            check=min(check, s.count(i)/target.count(i))
        return check
