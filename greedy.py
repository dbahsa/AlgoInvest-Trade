from csv import reader


# Getting stocks data from the first table provided by the customer
stocks = []
with open('data/data0.csv', 'r') as f:
    stocks = [tuple(x) for x in list(reader(f))]
# for i in stocks:
#     print(i)

