from csv import reader
#import time


# Getting shares data from the first table provided by the customer
shares = []
with open('data/data0.csv', 'r') as f:
    shares = [tuple(x) for x in list(reader(f))]
shares.pop(0)

shares = sorted(shares, key=lambda share: int(share[1]))

# realshares takes into account profit in * not in % (gain of at list 3.5 sec of computation)
realshares=[]
for i in range(len(shares)):
    a=[]
    c=list(shares[i])
    a.append(shares[i][0])
    a.append(int(float(shares[i][1])))
    a.append(round((float(shares[i][1])*float(shares[i][2])/100), 2))
    realshares.append(tuple(a))


for p in realshares:
    print(p[1])
    # print(p[1])
    # print(p[2])
    # if p[1].isdigit():
    #     print(p)
# print(len(realshares))


'''
################# I. GREEDY/NAIVE APPROACH ==> yields 133.56€ ######################
# With the Greedy solution, we only take the highest ROI (roi = return on investment), that does not exceed the $500 budget investment limit. It's simple, but not guaranteed to be optimal.

def naive_solution(shares, budget):
    """function to compute the highest earnings using the greedy/naive solution"""
    
    # budget = amount invested to buys shares
    # sort shares by roi, descending order:
    shares = sorted(shares, key=lambda share: int(share[2]), reverse=True)
    chosen_shares = {}
    total_gain = 0
    for i in range(len(shares)):
        # name: share name
        # cost: share price
        name, cost, roi  = shares[i]
        # quantity_of_share: we used floor division to get the max num of shares out of the budget invested
        
        if budget >= int(cost):

            quantity_of_share = budget // int(cost)
            chosen_shares[name] = quantity_of_share
            
            # update the budget amount (use only what's remained)
            budget -= quantity_of_share * int(cost)
            
            # this budget update works too: budget = budget % int(cost)
            total_gain += quantity_of_share*int(cost)*int(roi)/100
            
            # the total_gain is the quantity of a particular share * its roi in € (here, it's computed using int(cost)*int(roi)/100); otherwise put, with any share your earn x amount of € based on its roi, in our case here, with one share of Action-10, the yield is 9.18€. so if you buy 14 of them, you'll earn 14*9.18€=128.52€... and if you add up the one share of Action-19, your total earning is 133.56€.
    
    return f"{round(total_gain, 2)}€", chosen_shares

print(naive_solution(shares, 500)) ## yields 133.56€

'''

########## BINARY SEARCH ##########
'''my_list = [1,3,5,7,9,10,11]

def binary_search(list, item):
  low = 0
  high = len(list)-1
  while low <= high:
    mid = (high + low)//2
    guess = list[mid]
    if guess == item:
      return mid
    elif guess < item:
      low = mid + 1
    else:
      high = mid - 1
  return None


print(binary_search(my_list, 5))
print(binary_search(my_list, -1))'''



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
