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



############# OPTIMIZED SOLUTION ==> yields Intermediary value of 227 <=> to 91.72€ found with Brute Force##############

def dynamic_solution(budget, shares):
    """function to compute the highest earnings using .... solution"""

    # matrix is set to make the computation starting from 0 budget to its max capacity
    matrix = [[0 for x in range(budget+1)] for x in range(len(shares)+1)]
    # budget+1: to fill in when the budget is null
    # len(shares)+1: to fill in when there's no shares (none used or taken yet)
    # print(matrix)

    # go through each share
    for i in range(1, len(shares)+1):
        # go through / check according to budget size
        for w in range(1, budget+1):
            # check if the cost of the current share <= budget in order to add it
            if int(shares[i-1][1]) <= w:
                matrix[i][w] = max(int(shares[i-1][2]) + int(matrix[i-1][w-int(shares[i-1][1])]), int(matrix[i-1][w]))
            else:
                matrix[i][w] = matrix[i-1][w]
    
    # compute
    w = budget
    n = len(shares)
    chosen_shares = []

    while w >= 0 and n >= 0:
        e = shares[n-1]
        if matrix[n][w] == matrix[n-1][w-int(e[1])] + int(e[2]):
            chosen_shares.append(e)
            w -= int(e[1])
        
        n -= 1
    
    return matrix[-1][-1], chosen_shares

print(dynamic_solution(500, shares))
