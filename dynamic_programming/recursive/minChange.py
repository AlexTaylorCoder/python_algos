def rec_change(amount, coins,memo={}):
  if amount in memo:
    return memo[amount]
  if amount == 0:
    memo[amount] = 0
    return 0
  #Need to maintain count for path
  #shortest path
  min_coins = float("inf")
  for coin in coins:
    if amount-coin >= 0:
      num_coints = rec_change(amount-coin,coins) + 1
      if num_coints < min_coins:
        min_coins = num_coints
  memo[amount] = min_coins
  return min_coins

def min_change(amount,coins):
  ans = rec_change(amount,coins)
  return -1 if ans == float("inf") else ans
