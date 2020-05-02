def printHangman(N):
    print("\t____")
    print("\t|  |")
    print("\t|  ", end="")
    if N > 0:
        print("O")
    else:
        print()
    print("\t| ", end="")
    if N > 2:
        print("/", end="")
    else:
        print(" ", end="")
    if N > 1:
        print("|", end="")
    else:
        print(" ", end="")
    if N > 3:
        print("\\")
    else:
        print(" ")
    print("\t| ", end="")
    if N > 4:
        print("/ ", end="")
    else:
        print("  ", end="")
    if N > 5:
        print("\\")
    else:
        print(" ")
    print("\t|")
    print("-------------")

def win(d):
    print ('Your word looks like this')
    print (userguessresult)
    print ('\n')
    printHangman(d)
    print ('\n')
    print ('Your points so far : %d' % (points))


def inputstr(a):
    print ('Your word looks like this')
    print (userguessresult)
    print ('\n')
    printHangman(a)
    print ('\n')
    print ('Your points so far : %d' % (points))
    print ('You\'ve entered (wrong): %s' % (userguessedwrong))
    print ('\n')
    k=input ('Choose a letter :')
    print ('*' *50)
    return k
    
def assembleuserguessresult(c):
    strtemp2 = ''
    for i in range(0, len(userguessresult)):
        if userguessresult[i] == '*' and strtemp[i] == '*':
            strtemp2 = strtemp2 + '*'
        elif userguessresult[i] != '*':
            strtemp2 = strtemp2 + userguessresult[i]
        elif strtemp[i] != '*' :
            strtemp2 = strtemp2 + strtemp[i]
    return strtemp2

#main function
secretword = 'pneumonoultramicroscopicsilicovolcanoconiosis'
misstimes = 0
flag_continue = True
userguessresult = '*' * len(secretword)
points = 0
userguessedwrong = ''
while misstimes < 6:
    userguess = inputstr(misstimes)
    flag_guess = False
    strtemp = ''
    for i in range(0, len(secretword)):
        if secretword[i] == userguess :       
            flag_guess = True
            #userguessresult = userguessresult[0:i] + secretword[i] + userguessresult[i+1:]
            strtemp = strtemp + secretword[i]
        else :
            strtemp = strtemp + '*'
    userguessresult = assembleuserguessresult(strtemp)              
    if flag_guess == True:
        points = points + 1
    else:   
        userguessedwrong = userguessedwrong + userguess + ',' + ' '
        misstimes = misstimes + 1                
    if userguessresult == secretword :
        win(misstimes)
        print ('You win')
        break
else:
    printHangman(6)
    print ('you lose')
