class Solution(object):
    def haveConflict(self, event1, event2):
        s_e1 = int(event1[0].split(':')[0])*60+int(event1[0].split(':')[1])
        e_e1 = int(event1[1].split(':')[0])*60+int(event1[1].split(':')[1])

        s_e2 = int(event2[0].split(':')[0])*60+int(event2[0].split(':')[1])
        e_e2 = int(event2[1].split(':')[0])*60+int(event2[1].split(':')[1])
        
        if s_e1<s_e2 and e_e1<s_e2:
            return False
        elif s_e2<s_e1 and e_e2<s_e1:
            return False
        else:
            return True
