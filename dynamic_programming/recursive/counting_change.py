def counting_change(amount,coins,ways = 0):
  if amount == 0:
    return True
  if amount < 0:
    return False
  for coin in coins:
    change = counting_change(amount-coin,coins,ways)
    if change:
      ways += 1
  return ways
