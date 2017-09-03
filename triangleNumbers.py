import itertools

def triangleNumber(x):
    sum = 0
    i = 0
    while i<=x:
        sum+=i
        i+=1
    return sum

def numDivisors(x):
    num = 0
    i = 1
    sqrt = (x**0.5)-((x**0.5)%1)
    while (i<=(sqrt+1)):
        if x%i == 0:
            num+=2
        i+=1 
    return num   

def compute():
    	triangle = 0
	for i in itertools.count(1):
		triangle += i  # This is the ith triangle number, i.e. num = 1 + 2 + ... + i = i * (i + 1) / 2
		if numDivisors(triangle) > 500:
			break
	return str(triangle)

print(compute())

