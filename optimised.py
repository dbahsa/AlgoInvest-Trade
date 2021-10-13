from csv import reader
import time


# Getting shares data from the first table provided by the customer
shares = []
with open('data/data0.csv', 'r') as f:
    shares = [tuple(x) for x in list(reader(f))]
shares.pop(0)
# realshares takes into account profit in * not in % (gain of at least 3.5 sec of computation)
realshares=[]
for i in range(len(shares)):
    a=[]
    a.append(shares[i][0])
    a.append(int(shares[i][1]))
    a.append(round((int(shares[i][1])*float(shares[i][2])/100), 2))
    realshares.append(tuple(a))

############# OPTIMIZED SOLUTION ##############

def dynamic_solution(budget, realshares):
    """Function to compute the highest investment return, using bottom-up DP solution for a 0-1 Knapsack problem"""

    # table is set to allow computation to start from 0 budget and 0 share to both max capacities
    table = [[0 for x in range(budget+1)] for x in range(len(realshares)+1)]
    # budget+1: to fill in when the budget is null
    # len(realshares)+1: to fill in when there's no share (none used)

    # go through each 'ai' share
    for ai in range(len(realshares)+1):
        # for each 'ai' share, check available 'bi' budget
        for bi in range(budget+1):
            # 'ci' is the cost of each 'ai' share
            ci = realshares[ai-1][1]
            # let's check if the cost of the current share <= budget in order to add it in the table
            if ai == 0 or bi == 0: 
                table[ai][bi] = 0
                # This part of the code is responsible for setting the 0th row and column to 0.
                # Add into the table the max of realshares obtained between the line before 'table[ai-1][bi]' and the max of the current share + the optimised solution minus the item from the preceding line 
                # table[ai][bi] = max(realshares[ai-1][2] + table[ai-1][bi-ci], table[ai-1][bi])
            elif ci <= bi:
                #This following line checks that the cost of the 'ai' share is less than the total cost allowed for that cell (bi).
                # 'pi' is the profit of the current 'ai' share being computed
                pi = realshares[ai-1][2]
                #This line below checks that the cost of the 'ai' share is less than the total cost allowed for that cell (bi).
                table[ai][bi] = max(pi + table[ai-1][bi-ci],  table[ai-1][bi])
                # 'table[ai-1][bi-ci]' is the preceding profit
                # This helps to select the maximum out of the two options available to us. We can either include the share or exclude it.
                # Here, table[ai – 1][bi] means that 'ai' share is not included.
            else: 
                table[ai][bi] = table[ai-1][bi]
                # This part of the loop is accessed when the cost of 'ai' share is greater than the allowed 'bi'.
    # COMPUTATION
    b = budget
    n = len(realshares)
    chosen_shares = []
    while b >= 0 and n >= 0:
        # 'a': current share
        a = realshares[n-1]
        if table[n][b] == table[n-1][b-a[1]] + a[2]:
            chosen_shares.append(a)
            b -= a[1]
        n -= 1
    return table[-1][-1], chosen_shares


print()
# START TIMER
start = time.time()
# BUDGET LIMIT
budget = 500
dp = dynamic_solution(budget, realshares)
# PRINTING OUTPUT I
print(f'\nAvec un budget de "{budget}€", on peut gagner "{round(dp[0], 2)}€" de bénéfice en créant un porteuille qui comprend les actions suivantes:\n')
print('Action: Coût, Bénéfice en €')
print('----------------------------')
final_cost=[]
for x in dp[1]:
    print(f'{x[0]}: {x[1]}€ , {x[2]}€')
    final_cost.append(x[1])
# END TIMER
end = time.time()
# PRINTING OUTPUT II
print()
print(f"Coût Total: {round(float(sum(final_cost)), 2)}€")
print(f"Bénéfice Total: {round(dp[0], 2)}€")
print(f"Durée d'exécution: {round((end-start), 4)} sec")
print()
