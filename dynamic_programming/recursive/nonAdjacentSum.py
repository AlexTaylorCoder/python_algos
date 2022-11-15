def non_adjacent_sum(nums,i=0,memo={}):
  #Add all elements up to get highest
  #Reduce highest 
  if i in memo:
    return memo[i]
  if len(nums) <= i:
    return 0

  include = nums[i] + non_adjacent_sum(nums,i+2,memo)
  exclude = non_adjacent_sum(nums,i+1,memo)
  
  memo[i] = max(include,exclude)
  return memo[i]

nums = [7, 5, 5, 12, 17, 29]
print(non_adjacent_sum(nums)) # -> 48