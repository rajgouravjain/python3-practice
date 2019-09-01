"""You
are
given
the
stock
quotes
of
a
company
for the next ‘n’ days.Write a method to find the best day to buy the stock and the best day to sell the stock such that we make the maximum the profit.We can buy the stock only once and sell the stock only once.

Example: Say
the
data is [10, 30, 80], you
would
buy
on
the
1
st
day and sell
on
the
3
rd
day.
"""
l = [50, 30, 10, 80]
l = [(80, 0), (10, 1), (30, 2)]
from operator import itemgetter

d = zip(l, range(len(l)
## d = [ (10, 0), (80,1), (80,2) (30,3) ]
sorted_d = sorted(d, key=lambda i: itemgetter(i[0], i[1])
## sorted_d = [ (10, 1), (30,2), (80,0) ]
max_profit = 0
max_profit_buy_days = 0
max_profit_buy_sells = 0

for buy_i in (range(len(l) - 1):
    for
sell_i in (range(j + 1, len(l)):
if max_profit < sorted_d[sell_i][0] > sorted_d[buy_i][0]
    max_profit = sorted_d[sell_i][0] - sorted_d[buy_i][0]
    max_profit_buy_days = buy_i
    max_profit_buy_sells = sell_i

##buy_index +1 day I will buy

##sell_element+1 day I will sell
