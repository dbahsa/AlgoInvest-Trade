from csv import reader
import time
import math


# Getting shares data from the first table provided by the customer
shares = []
with open('data/client_data2.csv', 'r') as f:
    shares = [tuple(x) for x in list(reader(f))]
# REMOVE TITLE
shares.pop(0)
# CONVERTING TO 'EUROS' TO 'CENTIMES EUROS'
realshares=[]
for i in range(len(shares)):
    share_name = shares[i][0]
    share_cost = int(float(shares[i][1])*100)
    share_perct_gain = float(shares[i][2])
    share_euro_gain = share_cost * share_perct_gain/100
    realshares.append(tuple([share_name, share_cost, share_euro_gain]))
# REMOVE SHARES WITH NEGATIVE COST AND PROFIT
used_shares=[]
not_used_shares=[]
for p in realshares:
    if p[1] >= 0 and p[2]>0:
        used_shares.append(p)
    else:
        not_used_shares.append(p)


############# OPTIMIZED SOLUTION 2 ##############

def dynamic_solution(budget, used_shares):
    """Function to compute the highest earnings using bottom up DP solution"""

    table = [[0 for x in range(budget+1)] for x in range(len(used_shares)+1)]
    for i in range(len(used_shares)+1):
        for j in range(budget+1):
            if i == 0 or j == 0: 
                table[i][j] = 0
            elif used_shares[i-1][1] <= j: 
                table[i][j] = max(used_shares[i-1][2] + table[i-1][j-used_shares[i-1][1]],  table[i-1][j]) 
            else: 
                table[i][j] = table[i-1][j]
    j = budget
    n = len(used_shares)
    chosen_shares = []
    while j >= 0 and n >= 0:
        e = used_shares[n-1]
        if table[n][j] == table[n-1][j-e[1]] + e[2]:
            chosen_shares.append(e)
            j -= e[1]
        n -= 1
    return table[-1][-1], chosen_shares


print()
start = time.time()
budget = 500*100
a = dynamic_solution(budget, used_shares)
print(f'\nAvec un budget de "{round(budget/100, 2)}€", on peut gagner "{round((a[0])/100, 2)}€" de bénéfice en créant un porteuille qui comprend les actions suivantes:\n')
print('Action:\t\tCoût')
print('------------------------')
real_tot_cost=[]
for x in a[1]:
    real_tot_cost.append(x[1])
    if x[2] > 0:
        print(f'{x[0]}:\t{round(((x[1])/100), 2)}€')
end = time.time()
print()
print(f"Coût total: {round(sum(real_tot_cost)/100, 2)}€")
print(f'Durée d\'exécution: {round((end-start), 2)} sec')
print()
