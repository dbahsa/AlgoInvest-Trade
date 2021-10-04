from csv import reader
import time


# Getting shares data from the first table provided by the customer
shares = []
with open('data/data0.csv', 'r') as f:
    shares = [tuple(x) for x in list(reader(f))]
shares.pop(0)
# shares = sorted(shares, key=lambda share: share[0])

# realshares takes into account profit in * not in % (gain of at list 3.5 sec of computation)
realshares=[]
for i in range(len(shares)):
    a=[]
    # c=list(shares[i])
    a.append(shares[i][0])
    a.append(int(shares[i][1]))
    a.append(round((int(shares[i][1])*float(shares[i][2])/100), 2))
    realshares.append(tuple(a))


############# OPTIMIZED SOLUTION 1 ##############

def dynamic_solution(budget, realshares):
    """function to compute the highest earnings using bottom up DP solution"""

    # table is set to allow computation to start from 0 budget and 0 share to both max capacities
    table = [[0 for x in range(budget+1)] for x in range(len(realshares)+1)]
    # budget+1: to fill in when the budget is null
    # len(realshares)+1: to fill in when there's no share (none used)
    # print(table)

    # go through each share
    for i in range(len(realshares)+1):
        # for each share, check available budget
        for j in range(budget+1):
            # check if the cost of the current share <= budget in order to add it
            
            # if realshares[i-1][1] <= j:
            if i == 0 or j == 0: 
                table[i][j] = 0
                # This part of the code is responsible for setting the 0th row and column to 0.

                """# add into the table the max of realshares obtained between the line before (int(table[i-1][j])) and the max of the current share + la solution optimisée moins l'element de la ligne d'avant
                # table[i][j] = max(realshares[i-1][2] + table[i-1][j-realshares[i-1][1]], table[i-1][j])"""
            
            elif realshares[i-1][1] <= j:
                #This line of code checks that the cost of the i(th) share is less than the total cost allowed for that cell (j).

                table[i][j] = max(realshares[i-1][2] + table[i-1][j-realshares[i-1][1]],  table[i-1][j])
                # The line above is responsible for selecting the maximum out of the two options available to us. We can either include the share or exclude it.

                # Here the term table[i – 1][j] means that ith share is not included. The term val[i – 1] + table[i – 1][j – wt[i – 1]] represents that the ith share is included.

            else: 
                table[i][j] = table[i-1][j]
                # This part of the loop is accessed when the cost of ith share is greater than the allowed limit (j).
    
    # compute
    j = budget
    n = len(realshares)
    chosen_shares = []

    while j >= 0 and n >= 0:
        e = realshares[n-1]
        if table[n][j] == table[n-1][j-e[1]] + e[2]:
            chosen_shares.append(e)
            j -= e[1]
        
        n -= 1
    
    return table[-1][-1], chosen_shares

start = time.time()
print()

budget = 500
a = dynamic_solution(budget, realshares)

print(f'\nAvec un budget de "{budget}€", on peut ganger "{round(a[0], 2)}€" de bénéfice en créant un porteuille qui comprend les actions suivantes:\n')
print('Action: Coût, Bénéfice en €')
print('----------------------------')
# m=0
final_cost=[]
for x in a[1]:
    print(f'{x[0]}: {x[1]}€ , {x[2]}€')
    # m+=x[2]
    final_cost.append(x[1])
end = time.time()
print()
# print(f'{m}€')
print(f"Coût Total: {sum(final_cost)}€")
# print()
print(f"Durée d'exécution: {round((end-start), 4)} s.")
print()

