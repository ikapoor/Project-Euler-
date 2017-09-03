def fibb(n):
    if (n ==1):
        return 1
    elif (n == 2):
        return 2

    else:
        return (fibb(n-1) + fibb(n-2))

sum = 0
i = 1
while (fibb(i)<4000000):
    if (fibb(i)%2 == 0):
        sum += fibb(i)
    i = i+1

print (sum)
