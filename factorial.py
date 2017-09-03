def factorial(k):
    if (k==1):
        return 1
    if (k==0):
        return 1
    else:
        return(k*factorial(k-1))
def numDigits(num):
    numDig = 0
    while num > 0:
        num = num/10
        numDig += 1

    return numDig

def convertToArray(num):
    x = num
    a = []
    numDig = numDigits(num)
    while x >0:
        a.append(int(x/(10**(numDig-1))))
        x =( x -(x/(10**(numDig - 1)))*(10**(numDig - 1)))
        numDig = numDig - 1
    return a
b = convertToArray(factorial(100))

print b

sum  = 0

for x in range(len(b)-1):
    sum += b[x]

print (sum)