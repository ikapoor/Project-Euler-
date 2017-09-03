def power(a,b):
    if b == 1:
            return a  
    else:
        return a*power(a,b-1)
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
        a.append(int((x/(10**(numDig-1)))))
        x =( x -(x/(10**(numDig - 1)))*(10**(numDig - 1)))
        numDig = numDig - 1
    return a

d = convertToArray(power(2,999)*2)
sum = 0
for x in range(len(d)):
    sum+=d[x]

print (sum)


