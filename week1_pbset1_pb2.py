
"""
Problem 2
0/10 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob'
occurs in s. For example, if s = 'azcbobobegghakl',
then your program should print

Number of times bob occurs is: 2



"""
#define s
s = 'bjobobqvoboobooboobob'

numBob = 0
myId = 0

for char in s:
    if s[myId:myId+3]=="bob":
    #if s[myId:myId]=="b" and s[myId:myId+1]=="o"and s[myId:myId+2]=="b"     
        numBob += 1
    print("myId : " + str(myId) + ", numBob : " + str(numBob) )
    myId += 1

print(len(s))
print('Number of times "bob" occurs is : ' + str(numBob))


