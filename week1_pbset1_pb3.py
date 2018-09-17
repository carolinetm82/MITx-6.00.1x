
print ("OK")
print("")
s = 'abcdefghijklmnopqrstuvwxyz'
MyStr = s
long_str_current = ""
long_str_total  = ""

for i in range(len(MyStr)-1):
        if long_str_current == "":
            long_str_current +=MyStr[i]
            print("ancienne chaine_actuelle:",long_str_current)
        if(MyStr[i] <= MyStr[i+1]):
              long_str_current +=MyStr[i+1]
              print("chaine_actuelle si pre_car < next_car:",long_str_current)
        else:
              long_str_current=MyStr[i+1]  
              print("chaine_actuelle si pre_car > next_car:",long_str_current)
        if len(long_str_current) > len(long_str_total) :
              long_str_total=long_str_current
        elif s in 'zyxwvutsrqponmlkjihgfedcba':
              long_str_total=MyStr[0]
print("La plus longue chaîne est:",long_str_total)


print("")
print ("Code de William")
print("")
s = 'abcdefghijklmnopqrstuvwxyz'
MyStr = s
long_str_current = ""
long_str_total  = ""

for i in range(len(MyStr)-1):
        if long_str_current == "":
             long_str_current +=MyStr[i]
             print("ancienne chaine_actuelle:",long_str_current)
             
        if(MyStr[i] <= MyStr[i+1]):
              long_str_current += MyStr[i]
              print("chaine_actuelle:",long_str_current)
              
        elif len(long_str_current + MyStr[i+1]) > len(long_str_total) :
            print(long_str_current + " <-compare to-> " + long_str_total + " > " + str(len(long_str_current) > len(long_str_total)))
            long_str_current += MyStr[i]
                
            long_str_total = long_str_current
            #print("chaine_totale:",long_str_total)
            #print("")
            print("chaine_totale:" + long_str_total + "\n")
            long_str_current = ""

        else:
            long_str_current = ""
print("La plus longue chaîne est:",long_str_total)


print("")
print ("Code de William sans les indices")
print("")
s = 'ppcjlobykixpcfjhmgxwxpdr'
# Paste your code into this box 
myCounter = 0
maxStr = ''

# main loop to remove the first character from s string
while len(s) > len(maxStr):
    lastChar = ''
    curMaxStr = ''
    
    for myChar in s:
        if lastChar <= myChar:
            curMaxStr += myChar
            lastChar = myChar
            print("la chaîne actuelle: ",curMaxStr)
            print("le dernier caractère: ",lastChar)
        else:
            break

    if len(curMaxStr) > len(maxStr):
        maxStr = curMaxStr
       
    s = s[1:]
    
#print(maxStr) 
print("Longest substring in alphabetical order is: " + maxStr)







s = 'abcdefghijklmnopqrstuvwxyz'
print("")
print ("Code pour EDX")
print("")
MyStr = s
long_str_current = ""
long_str_total  = ""

for i in range(len(MyStr)-1):
        if long_str_current == "":
            long_str_current +=MyStr[i]
            
        if(MyStr[i] <= MyStr[i+1]):
              long_str_current +=MyStr[i+1]
             
        else:
              long_str_current=MyStr[i+1]  
              
        if len(long_str_current) > len(long_str_total) :
              long_str_total=long_str_current
        elif s in 'zyxwvutsrqponmlkjihgfedcba':
              long_str_total=MyStr[0]
print("La plus longue chaîne est:",long_str_total)
