#Project Euler Problem 25: N-digit Fibonacci number

from math import log10, ceil, sqrt
phi = (1+sqrt(5))/2 
d = int(input("Digits in Fibonacci number?"))

term = ceil((d-1 + log10(5)/2) / log10(phi))
print "Term #%d is the first term in the Fibonacci sequence to contain %d digits" % (int(term), d)