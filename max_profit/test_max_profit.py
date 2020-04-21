

def max_profit(prices):
  max = prices[1] - prices[0]
  for i, p1 in enumerate(prices[:-1]):
    for p2 in prices[i+1:]:
      profit = p2 - p1
      if profit > max:
        max = profit
        buy_max = p1
        sell_max = p2
  return(max)

def test_profits():
    assert max_profit([10, 7, 5, 8, 11, 9]) == 6
    