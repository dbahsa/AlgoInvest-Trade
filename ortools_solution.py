from ortools.algorithms import pywrapknapsack_solver
from csv import reader
import pandas as pd
# import pprint
import time
import math

# pp = pprint.PrettyPrinter(indent=4)

# Getting shares data from the first table provided by the customer
shares = []
with open('data/client_data2.csv', 'r') as f:
    shares = [tuple(x) for x in list(reader(f))]
shares.pop(0)


# realshares takes into account profit in * not in % (gain of at list 3.5 sec of computation)
realshares=[]
for i in range(len(shares)):
    share_name = shares[i][0]
    share_cost = int(float(shares[i][1]))
    share_perct_gain = float(shares[i][2])/100
    share_euro_gain = share_cost * share_perct_gain
    realshares.append(tuple([share_name, share_cost, share_euro_gain]))

used_shares=[]
not_used_shares=[]
# x=0
# for p in sorted(realshares, key=lambda share: share[1], reverse=True):
for p in realshares:
    # if p[1] >= 0 and p[2]>0:
    if p[1] >= 0 and p[2]>0:
        # print(p)
        used_shares.append(p)
        # x+=1
    else:
        not_used_shares.append(p)

############## OPTIMIZED WITH ORTOOLS ####################


def main():
    # Create the solver.
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

    names= []
    values = []
    a = []
    costs = [a]

    for i in range(len(used_shares)):
        names.append(used_shares[i][0])
        a.append(used_shares[i][1])
        values.append(used_shares[i][2])

    capacities = [500]

    solver.Init(values, costs, capacities)
    computed_value = solver.Solve()

    chosen_shares = {}
    packed_shares = []
    packed_names = []
    packed_costs = []

    total_earning = []
    total_cost = 0
    # print('Valeur Intermédiaire =', computed_value)
    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            packed_shares.append(i)
            packed_names.append(used_shares[i][0])
            packed_costs.append(costs[0][i])
            
            total_earning.append((used_shares[i][2]))
            
            x = {}
            # x["Action"] = used_shares[i][0]
            if costs[0][i] > 0:
                x["Coût"] = costs[0][i]
                x["Action"] = used_shares[i][0]
            
            chosen_shares[i] = x 
            
            total_cost += costs[0][i]

    print(f'\nCoût Total: {round((total_cost), 2)}€')
    print(f'Bénéfice Totale: {round(sum(total_earning), 2)}€')

    print()
    ''' Without Pandas, use the lines below:
    # print('Noms des actions:', packed_names)
    # print('Indexes Actions:', packed_shares)
    # print('Coûts des actions:', packed_costs)
    # print()'''
    
    # pp.pprint(chosen_shares)
    # for k in chosen_shares:
    #     pp.pprint(k)
    
    # print()
    df = pd.DataFrame(chosen_shares)
    # dropna() used to removed null in df
    print(df.T.dropna())



if __name__ == '__main__':
    start = time.time()
    print()

    main()
    
    end = time.time()
    print()
    print(f'{round((end-start), 5)} sec')
    print()
