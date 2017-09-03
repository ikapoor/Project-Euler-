import math

def getFactors(n):
    factors = []
    i = 1
    while(i<=math.sqrt(n)):
        if (n%i == 0 ):
            factors.append(i)
            if(i!=math.sqrt(n) and i !=1):
                factors.append(int(n/i))
        i+=1
    
    return factors


def isAmicable(n):
    factors = getFactors(n)
    inverse = sum(i for i in factors)
    inverseFactors = getFactors(inverse)
    sumOfInverseFactors = sum(i for i in inverseFactors)
    if (sumOfInverseFactors == n and inverse!=n):
        return True
    return False

    

amicableNumbers = []

for i in range(10000):
    if isAmicable(i):
        amicableNumbers.append(i);

print (amicableNumbers)
print(sum(i for i in amicableNumbers))
    
     