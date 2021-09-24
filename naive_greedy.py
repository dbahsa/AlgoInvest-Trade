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


################# I. GREEDY/NAIVE APPROACH ######################
# I. GREEDY APPROACH ==> yields 133.56€
# With the Greedy approximation, we only take the highest ROI (roi = return on investment), that does not exceed the $500 capital investment limit. It's simple, but not guaranteed to be optimal.

def naive_solution(shares, capital):
    """function to compute the highest earnings using the greedy/naive solution"""
    
    # capital = amount invested to buys shares
    # sort shares by roi, descending order:
    shares = sorted(shares, key=lambda share: int(share[2]), reverse=True)
    chosen_shares = {}
    profit = 0
    for i in range(len(shares)):
        # name: share name
        # cost: share price
        name, cost, roi  = shares[i]
        # quantity_of_share: we used floor division to get the max num of shares out of the capital invested
        
        if capital >= int(cost):

            quantity_of_share = capital // int(cost)
            chosen_shares[name] = quantity_of_share
            # update the capital amount (use only what's remained)
            capital -= quantity_of_share * int(cost)
            # this capital update works too: capital = capital % int(cost)
            profit += quantity_of_share*int(cost)*int(roi)/100
            # the profit is the quantity of a particular share * its roi in € (here, it's computed using int(cost)*int(roi)/100); otherwise put, with any share your earn x amount of € based on its roi, in our case here, with one share of Action-10, the yield is 9.18€. so if you buy 14 of them, you'll earn 14*9.18€=128.52€... and if you add up the one share of Action-19, your total earning is 133.56€.
    return f"{round(profit, 2)}€", chosen_shares

print(naive_solution(shares, 500)) ## yields 133.56€






############# II RECURSION (WITH FIBONACCI) WILL HELP MAKE AN OPTIMAL CHOICE FOR SELECTING MORE LUCRATIVE SHARES #############
# 1. Generate all possible combinations
# 2. Evaluate and choose the best combination
# it will give: n items, 2**n Outcomes.  This algorithm is O(2^n) => good way of solving, but not practical (too slow ==> Time complexity: T(n-1)+T(n-2), Exponential).
# Memoization is then used to fix this issue (see below with the 2 fibonacci functions)





''' IT DOES WORK ... JUST GOTTA ADD DATA TO IT :(
####################### III. MEMOIZATION APPROACH ###############
# II.1 FIBONACCI: Goal is to write function to return nth term of Fibonacci Sequence (fast, clearly written and rock solid)

########## Without functools  #########
# to fix Fibonacci slow computation, we use Memoization
# Time complexity: Linear. Each number must be computed only once since it is stored in the memo.

fibonacci_cache = {}

def fibonacci(n):
    # if we had cached the value, then return it 
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    # compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
    
    # Cache the value and return it
    fibonacci_cache[n] = value
    return value

# for n in range(1, 101):
#     print(n, ":", fibonacci(n))


####### Fix Fibonacci slow computation with 'functools' ########

from functools import lru_cache
# to add memoization to the following function

# lru_cache used as a decorator. maxsize default value = 128
@lru_cache(maxsize=1000)
def fibo(n):
    """recursive function"""
    # check that the input is an intger
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    # Compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibo(n-1) + fibo(n-2)

for n in range(1, 51):
    print(fibo(n))
'''



'''def generate(n):
  series = [1,1]
  for idx in range(2,n+1):
    series.append(series[idx-1]+series[idx-2])
  return series[-1]
start = time.time()
print(generate(50))
end = time.time()
print(end-start)
'''
