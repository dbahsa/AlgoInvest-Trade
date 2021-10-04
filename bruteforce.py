from csv import reader
# from functools import lru_cache
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
    # c=list(shares[i])
    a.append(shares[i][0])
    a.append(int(shares[i][1]))
    a.append(round((int(shares[i][1])*int(shares[i][2])/100), 2))
    realshares.append(tuple(a))


############# BRUTE FORCE (or Exhaustive Search) yields 99.08€€  ### O(2^20) ##############

# Brute force will check all possible outcomes that can be created with a given budget
def brute_force_solution(budget, realshares, final_chosen_shares=[]):
    """function to compute the highest earnings using brute force algorithm"""
    
    # shares is used as our base point (le point d'arrêt pour la fct° recursive ci-après), as long as there's an item in shares, the algo will keep on computing
    if realshares:
        
        #profit_one will ignore starting_share
        profit_one, chosen_shares_for_profit_one = brute_force_solution(budget, realshares[1:], final_chosen_shares)
        
        starting_share = realshares[0]

        if starting_share[1] <= budget:
            # starting_share[1] is the cost of the starting_share chosen above
            profit_two, chosen_shares_for_profit_two = brute_force_solution(budget - starting_share[1], realshares[1:], final_chosen_shares + [starting_share])
            
            if profit_one < profit_two:
                return profit_two, chosen_shares_for_profit_two
        
        return profit_one, chosen_shares_for_profit_one
    else:
        return round(sum([i[2] for i in final_chosen_shares]), 2), final_chosen_shares


start = time.time()

budget = 500
a = brute_force_solution(budget, realshares)

print(f'\nAvec un budget de "{budget}€", on peut ganger "{a[0]}€" de bénéfice en créant un porteuille constitué d\'actions suivantes:\n')
print('Action: Coût, Bénéfice en €')
print('----------------------------')
for x in a[1]:
    print(f'{x[0]}: {x[1]}€ , {x[2]}€')

end = time.time()
print()
print(f'{round((end-start), 2)} sec')
print()



########## BIG O NOTATION ##############
'''This works, but it’s really slow. For 3 shares, you have to calculate 8 possible sets. For 4 shares, you have to calculate 16 sets. With every share you add, the number of sets you have to calculate doubles! This algorithm takes O(2^n) time, which is very, very slow. Thus for 20 shares, it takes O(2^20) time to compute.

Therefore, we've got to calculate an approximate solution, which will be close to the optimal solution, but won't be the optimal solution.

This is when Dynamic Programming kicks in!

For the knapsack problem, we’ll start by solving the problem for smaller knapsacks (or “sub-knapsacks”) and then work up to solving the original problem.

'''