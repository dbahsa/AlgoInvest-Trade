from csv import reader
import time
import math


# Getting shares data from the first table provided by the customer
shares = []
with open('data/client_data2.csv', 'r') as f:
    shares = [tuple(x) for x in list(reader(f))]
shares.pop(0)


realshares=[]
for i in range(len(shares)):
    share_name = shares[i][0]
    share_cost = int(float(shares[i][1])*100)
    share_perct_gain = float(shares[i][2])
    share_euro_gain = share_cost * share_perct_gain/100
    realshares.append(tuple([share_name, share_cost, share_euro_gain]))
    # share_name = shares[i][0]
    # share_cost = int(float(shares[i][1]))
    # share_perct_gain = float(shares[i][2])
    # share_euro_gain = share_cost * share_perct_gain
    # realshares.append(tuple([share_name, share_cost, share_euro_gain]))

used_shares=[]
not_used_shares=[]
# x=0
# for p in sorted(realshares, key=lambda share: share[1], reverse=True):
for p in realshares:
    if p[1] >= 0 and p[2]>0:
    # if p[1] >= 0:
        used_shares.append(p)
    else:
        not_used_shares.append(p)


############# OPTIMIZED SOLUTION 2 ##############

def dynamic_solution(budget, used_shares):
    """function to compute the highest earnings using bottom up DP solution"""

    # table is set to allow computation to start from 0 budget and 0 share to both max capacities
    table = [[0 for x in range(budget+1)] for x in range(len(used_shares)+1)]
    # budget+1: to fill in when the budget is null
    # len(used_shares)+1: to fill in when there's no share (none used)
    # print(table)

    # go through each share
    for i in range(len(used_shares)+1):
        # for each share, check available budget
        for j in range(budget+1):
            # check if the cost of the current share <= budget in order to add it
            
            # if used_shares[i-1][1] <= j:
            if i == 0 or j == 0: 
                table[i][j] = 0
                # add into the table the max of used_shares obtained between the line before (int(table[i-1][j])) and the max of the current share + la solution optimisée moins l'element de la ligne d'avant
                # table[i][j] = max(used_shares[i-1][2] + table[i-1][j-used_shares[i-1][1]], table[i-1][j])
            
            elif used_shares[i-1][1] <= j: 
                table[i][j] = max(used_shares[i-1][2] + table[i-1][j-used_shares[i-1][1]],  table[i-1][j]) 
            else: 
                table[i][j] = table[i-1][j] 
            # else:
            #     table[i][j] = table[i-1][j]
    
    # compute
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

start = time.time()
print()

budget = 500*100
# budget = 500
a = dynamic_solution(budget, used_shares)

print(f'\nAvec un budget de "{round(budget/100, 2)}€", on peut ganger "{round((a[0])/100, 2)}€" de bénéfice en créant un porteuille qui comprend les actions suivantes:\n')
# print(f'\nAvec un budget de "{budget}€", on peut ganger "{(a[0])/100}€" de bénéfice en créant un porteuille qui comprend les actions suivantes:\n')
print('Action:\tCoût en centimes €')
print('----------------------------')
# m=0

real_tot_cost=[]
for x in a[1]:
    # print(f'{x[0]}: {x[1]} , {x[2]}')
    real_tot_cost.append(x[1])
    # m+=x[2]
    if x[2] > 0:
        # print(f'{x[0]}: {x[1]} , {x[2]}')
        print(f'{x[0]}:\t{x[1]}')
    
end = time.time()
print()
print(f"Coût total: {round(sum(real_tot_cost)/100, 2)}€")
# print(f"Coût total: {round(sum(real_tot_cost), 2)}€")
# print(f'{m}€')
# print()
print(f'{round((end-start), 4)} sec')
print()

