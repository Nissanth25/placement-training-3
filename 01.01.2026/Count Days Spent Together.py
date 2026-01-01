class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):

        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        arriveAlice = sum(days_in_months[:int(arriveAlice[:2])-1]) + int(arriveAlice[3:])
        leaveAlice = sum(days_in_months[:int(leaveAlice[:2])-1]) + int(leaveAlice[3:])
        arriveBob = sum(days_in_months[:int(arriveBob[:2])-1]) + int(arriveBob[3:])
        leaveBob = sum(days_in_months[:int(leaveBob[:2])-1]) + int(leaveBob[3:])
        gap = min(leaveAlice,leaveBob)-max(arriveAlice,arriveBob)
        return (gap+1 if gap >= 0 else 0)
