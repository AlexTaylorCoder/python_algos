def counting_change(amount,coins,i=0):
  #Wide Tree
  if i >= len(coins):
    return 0
  if amount == 0:
    return 1
  count = 0
  print(amount)
  while amount >= coins[i]:
    amount -= coins[i]
    count += counting_change(amount,coins,i+1)
  return count



print(counting_change(24, [5, 7, 3])) # -> 5