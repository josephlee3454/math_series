
def fibo_nth(n):
  """function that checks for fibonacci sequence"""
  if n == 1:
    return 1
  elif n == 2 :
    return 1
  else:
    return ( fibo_nth(n-1) + fibo_nth(n-2) )
print(fibo_nth(7))

def lucas_nth(n):
  """function that checks for lucas number sequence"""
  if n == 0:
    return 2
  if n == 1:
    return 1
  if n == 2:
    return 3
  else: 
    return (lucas_nth(n-1) + lucas_nth(n-2))
print(lucas_nth(2))

def sum_series(n, a=0, b=1):
  """"""
  if n == 0:
    return a
  elif n == 1:
    return b
  else: 
    return(sum_series(n-1, a, b) + sum_series(n-2, a, b))
print(sum_series(5,3,3))
  