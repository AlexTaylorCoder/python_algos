import math
def summing_squares(n):
  #Minimum number of perfect squares
  #Start at lower numbers and increase
  if n == 0:
    return 0
  minimum = float("infinity")
  for num in range(1,math.floor(math.sqrt(n))+1):
    count = summing_squares(n-num**num) + 1
    minimum = min(minimum,count)
  return minimum


print(summing_squares(8))