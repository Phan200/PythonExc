arr=[True] *(2*(10**9))

# su dung pp Sieve of Eratosthenes
def Sieve():
    p=2
    while p*p<=2*(10**9):
        if arr[p]==True:
            for i in range (p*p, 2*(10**9),p):
                arr[i]=False
            p+=1
def isPrime(n):
    if arr[n]==True: return True
    return False

Sieve()
t =int(input())
for _ in range(t):
    n = int(input())
    if isPrime(n):
        print("Prime")
    else: print("Not prime")
