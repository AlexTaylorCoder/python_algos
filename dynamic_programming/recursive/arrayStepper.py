def array_stepper(a):
  return _array_stepper(a,0)
  
def _array_stepper(a,i):
  if i >= len(a):
    return True
  if a[i] == 0:
    return False
  print(i,a[i])
  for num in range(1,a[i]+1):
    if _array_stepper(a,num+i):
      return True
  return False
  

print(array_stepper([2, 4, 2, 0, 0, 1]))