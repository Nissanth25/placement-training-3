class Solution(object):
    def countTime(self, time):
        hour, minutes = time.split(":")
        count_minutes, count_hour = 1, 1
        if hour[1] == '?' and hour[0] == '?' :
            count_hour = 24
        elif hour[0] == '?' :
            if int(hour[1]) < 4:
                count_hour=3
            else:
                count_hour =2
        elif hour[1] == '?':
            if int(hour[0]) <=1:
                count_hour = 10
            else:
                count_hour =4

        if minutes[0] == "?" and minutes[1] == "?":
            count_minutes= 60
        elif minutes[0] == '?' :
            count_minutes = 6
        elif minutes[1] == '?':
            count_minutes = 10
        
        return count_hour*count_minutes

