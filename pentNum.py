def isInt(k):
    if ( k %1 ==0):
        return True
    else:
        return False

def pentNumb(k):
    ans = (k*(3*k-1))/2
    return ans
pentagonNumbers = []

for x in range(10000):
    pentagonNumbers.append(pentNumb(x+1))


i = 0
while i < 9999:
    k = 0
    while k < 9999:
        if(((pentagonNumbers[i]-pentagonNumbers[k])in pentagonNumbers) and (((pentagonNumbers[i]+pentagonNumbers[k])in pentagonNumbers))):
            print (i,k)
        k+=1
    i+=1
