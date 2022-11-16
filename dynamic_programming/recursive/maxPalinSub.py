def max_palin_subsequence(string):
  # Start middle compare left and right 
  # If same continue comparing
  # If false split into left and right 
  return _max_palin_subsequence(string)
  
def _max_palin_subsequence(s):
  mid = len(s) // 2
  if mid == 1:
    return 1
  largest = float("-inf")
  print(largest)
  for i in range(mid):
    if s[mid + i]  != s[mid - i]:     
      sum = _max_palin_subsequence(s[:mid]) + _max_palin_subsequence(s[mid:])
      return max(largest,sum)
  return largest

  
print(max_palin_subsequence("luwxult")) # -> 5