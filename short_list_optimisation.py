from csv import reader
import time


# Getting shares data from the first table provided by the customer
shares = []
with open('data/data0.csv', 'r') as f:
    shares = [tuple(x) for x in list(reader(f))]
shares.pop(0)

# realshares takes into account profit in * not in % (gain of at list 3.5 sec of computation)
realshares=[]
for i in range(len(shares)):
    a=[]
    c=list(shares[i])
    a.append(shares[i][0])
    a.append(int(shares[i][1]))
    a.append(round((int(shares[i][1])*float(shares[i][2])/100), 2))
    realshares.append(tuple(a))


############# OPTIMIZED SOLUTION ==> yields Intermediary value of 227 <=> to 91.72€ found with Brute Force##############

def dynamic_solution(budget, realshares):
    """function to compute the highest earnings using .... solution"""

    # cell (from our table matrix) is set to allow computation to start from 0 budget and 0 share to both max capacities
    cell = [[0 for x in range(budget+1)] for x in range(len(realshares)+1)]
    # budget+1: to fill in when the budget is null
    # len(realshares)+1: to fill in when there's no share (none used)
    # print(cell)

    # go through each share
    for i in range(1, len(realshares)+1):
        # for each share, check available budget
        for w in range(1, budget+1):
            # check if the cost of the current share <= budget in order to add it
            if realshares[i-1][1] <= w:
                # add in the cell the max of realshares btained between the line before (int(cell[i-1][w])) and the max of the current share + la solution optimisée moins l'element de la ligne d'avant
                cell[i][w] = max(realshares[i-1][2] + cell[i-1][w-realshares[i-1][1]], cell[i-1][w])
            else:
                cell[i][w] = cell[i-1][w]
    
    # compute
    w = budget
    n = len(realshares)
    chosen_shares = []

    while w >= 0 and n >= 0:
        e = realshares[n-1]
        if cell[n][w] == cell[n-1][w-e[1]] + e[2]:
            chosen_shares.append(e)
            w -= e[1]
        
        n -= 1
    
    return cell[-1][-1], chosen_shares

start = time.time()
print()

# a= dynamic_solution(500, realshares)
a = dynamic_solution(500, realshares)
print(f'\nAvec un budget de 500€, on peut ganger "{round(a[0], 2)}€" de bénéfice en créant un porteuille constitué d\'actions suivantes:\n')
print('Action: Coût, Bénéfice en €')
print('----------------------------')
m=0
for x in a[1]:
    print(f'{x[0]}: {x[1]}€ , {x[2]}€')
    m+=x[2]
end = time.time()
print()
print(f'{m}€')
print()
print(f'{round((end-start), 2)} sec')
print()

