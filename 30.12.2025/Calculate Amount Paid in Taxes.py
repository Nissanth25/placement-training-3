class Solution(object):
    def calculateTax(self, brackets, income):
        tax = 0.0
        income_left = income
        for i, (upper, percent) in enumerate(brackets):
            upper_left = 0
            if i > 0:

                upper_left = upper - brackets[i-1][0]
            else:

                upper_left = upper

            if income_left >= upper_left:
                tax += upper_left*percent*0.01
                income_left -= upper_left
                
            else:
                tax += income_left*percent*0.01
                break

        return tax
            
