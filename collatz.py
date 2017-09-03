def nextCollatz(n):
    if (n%2==0):
        return n/2
    else:
        return (3*n +1 )


def collatzChainlength(n):
    i = 1
    while(n != 1):
        n = nextCollatz(n)
        i+=1
    return i

k = 1
maxchain = 0
maxnum = 1

while (k<1000000):
    p = collatzChainlength(k)
    if maxchain < p:
        maxchain = p
        maxnum = k

    k+=1


print (maxchain)
print (maxnum)

