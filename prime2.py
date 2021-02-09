import math
def isPrime(n):
    if (n==1 or n==0): return False
    if n==2: return True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True
t =int(input())
for _ in range(t):
    n = int(input())
    if isPrime(n):
        print("Prime")
    else: print("Not prime")
