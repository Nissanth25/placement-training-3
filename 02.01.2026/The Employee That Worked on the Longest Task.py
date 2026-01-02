class Solution(object):
    def hardestWorker(self, n, logs):
        highest_time = logs[0][1]
        id_of_highest = logs[0][0]

        for i in range(1,len(logs)):
            identity = logs[i][0]
            lt = logs[i][1] - logs[i-1][1]

            if lt > highest_time:
                highest_time = lt
                id_of_highest = identity

            elif lt == highest_time:
                if identity < id_of_highest:
                    id_of_highest = identity        


        return id_of_highest


