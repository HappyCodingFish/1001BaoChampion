import sys
sys.setrecursionlimit(3000)

def tryCode(n, memo={}):
  if n < 3: return 1
  if n in memo:
    return memo[n]
  
  memo[n] = tryCode(n-1) + tryCode(n-2)
  
  return memo[n]

# sys.stdout.write(tryCode(2999))

print(tryCode(2999))