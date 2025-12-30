class Solution(object):
    def bestHand(self, ranks, suits):
        dict_ranks = {}
        dict_suits = {} 

        answer = ""
        
        for x in range(len(ranks)): 
            if ranks[x] in dict_ranks:
                dict_ranks[ranks[x]] += 1

                if dict_ranks[ranks[x]] == 3:
                    answer = "Three of a Kind"

                if dict_ranks[ranks[x]] == 2 and answer != "Three of a Kind":
                    answer = "Pair"
            else:
                dict_ranks[ranks[x]] = 1 

            if suits[x] in dict_suits:
                dict_suits[suits[x]] += 1 

                if dict_suits[suits[x]] == 5: 
                    return "Flush"
            else: 
                dict_suits[suits[x]] = 1

        if answer == "":
            return "High Card"

        return answer



                

        
