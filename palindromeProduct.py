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
        a.append(x/(10**(numDig-1)))
        x =( x -(x/(10**(numDig - 1)))*(10**(numDig - 1)))
        numDig = numDig - 1
    return a

def reverseArray(list = []):
    rev = []
    length = len(list)-1
    for x in range(len(list)):
        rev.append(list[length])
        length = length - 1
    return rev



def isPalindrome(forw =[], rev = []):
    if (forw == rev):
        return True
    else:
        return False

first = 100

biggest = 0
while(first <999):
    second = 100
    while(second <999):
        product = first*second
        forward = convertToArray(product)
        reverse = reverseArray(forward)
        if (isPalindrome(forward,reverse)):
            if product > biggest:
                biggest = product
                print(biggest)
        second = second +1
    first = first + 1

print(biggest)
  
    
    
    




  
    

