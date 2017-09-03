def isDivisible(num,den):
    if den == 0:
        return False
    elif (num%den == 0):
        return True
    else:
        return False

def isprime(n):
    #make sure n is a positive integer
    n = abs(int(n))
    #0 and 1 are not primes
    if n < 2:
        return False
    #2 is the only even prime number
    if n == 2:
        return True
    #all other even numbers are not primes
    if not n & 1:
        return False
    #range starts with 3 and only needs to go up to the square root of n
    #for all odd numbers
    for x in range (3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True #if it makes it through all the catches, it is a prime


def factors(k):
    a = []
    for x in range(k+1):
        if (isDivisible(k,x)):
            a.append(x)

    return a

def isPrime(n):
    a = factors(n)
    if len(a) == 2:
        return True
    else:
        return False

def primeFactors(num):
    if (num == 1):
        return 1
    elif isPrime(num):
        return num
    PF = []
    NPF = []
    f = factors(num)
    for x in range(len(f)):
        if (isPrime(f[x])):
            PF.append(f[x])
        else:
            NPF.append(f[x])
    print(PF)
 


num = 600851475143 

for l in range(int(100000000)):
    if (isDivisible(num,l) and (isprime(num/l))):
        print num/l






    

        
