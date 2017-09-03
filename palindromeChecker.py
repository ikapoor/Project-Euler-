string  = str(input("Please Enter a word: "))
string = string.replace(" ","")

length = len(string)

forwardString = []
for x in range(len(string)):
    forwardString.append(string[x])


backwardsString = []

for x in range(len(string)):
    backwardsString.append(string[length-1])
    length = length -1

if (forwardString == backwardsString):
    print("You have entered a palindrome! :)")
else:
    print("You have not printed a palindrome! :(")
