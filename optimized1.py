from ortools.algorithms import pywrapknapsack_solver
from csv import reader
import pandas as pd
import pprint
#import time

pp = pprint.PrettyPrinter(indent=4)

# Getting shares data from the first table provided by the customer
shares = []
with open('data/data0.csv', 'r') as f:
    shares = [tuple(x) for x in list(reader(f))]
shares.pop(0)



def main():
    # Create the solver.
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

    names= []
    values = []
    a = []
    costs = [a]

    for i in range(len(shares)):
        names.append(shares[i][0])
        a.append(int(shares[i][1]))
        values.append(int(shares[i][2]))

    # print(names)
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
            packed_names.append(shares[i][0])
            packed_costs.append(costs[0][i])
            
            total_earning.append(int(shares[i][2])*int(shares[i][1])/100)
            
            x = {}
            x["Nom de l'action"] = shares[i][0]
            x["Coût de l'action"] = costs[0][i]
            
            chosen_shares[i] = x 
            
            total_cost += costs[0][i]

    print(f'\nCoût Total: {round(total_cost)}€')
    print(f'Bénéfice Totale: {round(sum(total_earning))}€')
    print()
    # print('Noms des actions:', packed_names)
    # print('Indexes Actions:', packed_shares)
    # print('Coûts des actions:', packed_costs)
    # print()
    
    # pp.pprint(chosen_shares)
    
    df = pd.DataFrame(chosen_shares)
    print(df.T)
    print()

if __name__ == '__main__':
    main()
