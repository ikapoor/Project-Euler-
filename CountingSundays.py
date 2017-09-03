def isLeapYear(n):
    if (n%400 == 0):
        return True
    if (n%100 == 0):
        return False
    if (n%4 == 0):
        return True
    
    return False

#input Jan 1st day, and if it is a leap year
#Sunday = 0
def NumSundaysinYear(n, LY):
    
    
    
    numSundays = 0
    if (n == 0):
        numSundays+=1
    n+=31
    if (n % 7== 0):
        numSundays+=1
    if (LY):
        n+=29
    else:
        n+=28
    if (n % 7== 0):
        numSundays+=1
    n+=31
    if (n % 7== 0):
        numSundays+=1
    n+=30
    if (n % 7== 0):
        numSundays+=1
    n+=31
    if (n % 7== 0):
        numSundays+=1
    n+=30
    if (n % 7== 0):
        numSundays+=1
    n+=31
    if (n % 7== 0):
        numSundays+=1
    n+=31
    if (n % 7== 0):
        numSundays+=1
    n+=30
    if (n % 7== 0):
        numSundays+=1
    n+=31
    if (n % 7== 0):
        numSundays+=1
    n+=30
    if (n % 7== 0):
        numSundays+=1
    
    return (numSundays)





print (NumSundaysinYear(0,False))

    
