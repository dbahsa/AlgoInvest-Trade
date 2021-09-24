from csv import reader
# from functools import lru_cache
#import time


# Getting shares data from the first table provided by the customer
shares = []
with open('data/data0.csv', 'r') as f:
    shares = [tuple(x) for x in list(reader(f))]
# Data header ('Actions #', 'Coût par action (en euros)', 'Bénéfice (après 2 ans)'):
# header = shares[0] 
# Remove the header in the csv file to allow sorting needed data
shares.pop(0)


############# BRUTE FORCE I: yields 227€  ### 2^20 ##############

# @lru_cache(maxsize=1000)
def brute_force_solution(budget, shares, chosen_shares=[]):
    """function to compute the highest earnings using brute force solution"""
    
    # shares is used as the breaking (stop) point for this recursive function
    if shares:
        val1, lstVal1 = brute_force_solution(budget, shares[1:], chosen_shares)
        val = shares[0]
        if int(val[1]) <= budget:
            val2, lstVal2 = brute_force_solution(budget - int(val[1]), shares[1:], chosen_shares + [val])
            if int(val1) < int(val2):
                return val2, lstVal2
        
        return val1, lstVal1
    else:
        # Brute force 1 => give the same result as with ortools module with an intermediary value of 227, we get 91.72€ total_gain:
        # return sum([int(i[2]) for i in chosen_shares]), chosen_shares
        
        # Brute force 2 yields 99€ total_gain:
        return round(sum([int(i[1])*int(i[2])/100 for i in chosen_shares])), chosen_shares

print(brute_force_solution(500, shares))
