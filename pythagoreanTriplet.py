def isPythagoreanTriplet(a,b):
    c = ((a*a+b*b)**0.5)
    if(c%1 == 0):
        return True
    else:
        return False

print (isPythagoreanTriplet(5,12))

i = 1
while 1<500:
    k = 1
    while k < 500:
        if((isPythagoreanTriplet(i,k)) and ((i + k + ((i*i+k*k)**0.5))== 1000)):
            print(i,k)
        k+=1
    i+=1