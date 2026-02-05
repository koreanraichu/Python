import sys
N = int(sys.stdin.readline())
prime = []

def isprime(a):
    sqrt = int(a ** 0.5)
    if a < 2:
        return False
    for i in range(2,sqrt+1):
        if a % i == 0:
            return False
    else: 
        return True

for i in range (N+1):
    if isprime(i):
        prime.append(str(i))
prime = ', '.join(prime)
print(prime)
