class Solution(object):
    def greatestLetter(self, s):
        letters=set(s)
        for ltr in sorted(letters, reverse=True):
            if ltr.isupper() and ltr.lower() in letters:
                return ltr

        return ''
