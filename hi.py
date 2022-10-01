print("Hi! Nice to meet you!")

def tryCode(n, memo={}):
  if n < 3: return 1
  if n in memo:
    return memo[n]
  
  memo[n] = tryCode(n-1) + tryCode(n-2)
  
  return memo[n]

print(trytCode(10))
