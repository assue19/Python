def total_params(*args):
  total= 0
  for i in args:
    total=total + i
  return total
print(total_params(10,25,60))