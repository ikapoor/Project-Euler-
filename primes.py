def isDivisible(a,b):
    if (a%b == 0):
        return True
    else: 
        return False

def isPrime(k):
    if k == 1:
        return False
    if k == 3:
        return True
    if k == 2:
        return True
    if (k%2 == 0):
        return False
        
    sqrt = int(k**0.5)
    i = 3
    prime = True;
    while(i<=sqrt):
        if (isDivisible(k,i)):
            prime = False
            break
        i+=2
    return prime

primes = []
primes.append(2)
currNum = 3

while (currNum < 2000000):
    if(isPrime(currNum)):
        primes.append(currNum)
    currNum+=2

print(primes)

sum = 0

for x in range(len(primes)):
    sum+=primes[x]

print (sum)
        
            
    
