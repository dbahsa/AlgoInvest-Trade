from csv import reader
import pandas as pd
import matplotlib.pyplot as plt



# Getting shares data from the first table provided by the customer
shares = []
with open('data/client_data2.csv', 'r') as f:
    shares = [tuple(x) for x in list(reader(f))]
# REMOVE TITLES FROM ORIGINAM FILE
shares.pop(0)
shares = sorted(shares, key=lambda share: share[1])
# CONVERT COSTS & PROFITS INTO FLOATS TO EASE COMPUTATIONS
realshares=[]
for i in range(len(shares)):
    share_name = shares[i][0]
    cost = float(shares[i][1])
    gain = float(shares[i][2])
    realshares.append(tuple([share_name, cost, gain]))
# PARSE DATA FOR ANALYSIS
used_shares=[]
not_used_shares=[]
for p in realshares:
    # p[1] >= 0 : to exclude neg valued shares // p[2]>0: to exclude non profitable shares
    if p[1] >= 0 and p[2]>0:
        used_shares.append(p)
    else:
        not_used_shares.append(p)

"""Used shares"""
# print()
# for k in used_shares:
#     print(k[0], "\t", f"{k[1]}€", "\t", f"{k[2]}€")
# print(len(used_shares))
# print()

"""Original shares"""
# print()
# for k in realshares:
#     print(k)
#     # print(k[0], "\t", f"{k[1]}€", "\t", f"{k[2]}€")
# print(len(realshares))
# print()

"""Excluded shares"""
# for k in not_used_shares:
#     print(k)
# print(len(not_used_shares))
# print()

"""Brute force graph data"""
# big_0_brute_force = [2**i for i in range(21)]
# for m in big_0_brute_force:
#     print(m)

"""Graphs"""
# df = pd.DataFrame(big_0_brute_force)
# df = pd.DataFrame(realshares)
# df = pd.DataFrame(used_shares)
df = pd.DataFrame(not_used_shares)

ax = df.plot.scatter(x=1 , y=2, alpha=0.5)
ax.set_xlabel('Coûts')
ax.set_ylabel('Profits')
# ax.set_title("Lot 1 - Actions Avec Valeurs Négatives")
# ax.set_title("Lot 1 - Actions Sans Valeurs Négatives")
# ax.set_title("Lot 1 - Action.s Exclue.s")
# ax.set_title("Lot 2 - Actions Avec Valeurs Négatives")
# ax.set_title("Lot 2 - Actions Sans Valeurs Négatives")
ax.set_title("Lot 2 - Actions Exclues")
plt.show()
