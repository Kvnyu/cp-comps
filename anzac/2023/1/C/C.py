import math
n = input()
n = int(n)

primes = {}
def is_prime(n):
  if n in primes:
    return primes[n]
  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      primes[n] = False
      return False
  primes[n] = True
  return True


steps = 0
curr = n
while curr >= 3:
    for i in range(3, curr, 2):
        if is_prime(i) and is_prime(curr-i):
            curr = (curr - i) - i 
            steps += 1
            break
print(steps)
