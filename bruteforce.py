from csv import reader
#import time


# Getting shares data from the first table provided by the customer
shares = []
with open('data/data0.csv', 'r') as f:
    shares = [tuple(x) for x in list(reader(f))]
# Data header ('Actions #', 'Coût par action (en euros)', 'Bénéfice (après 2 ans)'):
# header = shares[0] 
# Remove the header in the csv file to allow sorting needed data
shares.pop(0)


############# BRUTE FORCE I: yields 227€ ##############

def brute_force_solution(capital, shares, chosen_shares=[]):
    """function to compute the highest earnings using brute force solution"""
    
    if shares:
        val1, lstVal1 = brute_force_solution(capital, shares[1:], chosen_shares)
        # val1, lstVal1 = brute_force_solution(capital, shares, chosen_shares)
        val = shares[0]
        if int(val[1]) <= capital:
            val2, lstVal2 = brute_force_solution(capital - int(val[1]), shares[1:], chosen_shares + [val])
            if int(val1) < int(val2):
                return val2, lstVal2
        
        return val1, lstVal1
    else:
        # Brute force 1:
        # return sum([int(i[2]) for i in chosen_shares]), chosen_shares
        
        # Brute force 2 yields 99€ profit:
        return sum([int(i[1])*int(i[2])/100 for i in chosen_shares]), chosen_shares

print(brute_force_solution(500, shares))
