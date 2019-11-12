def palindromic(num1,num2):
    palindr = False
    num = num1*num2
    num_str = str(num)
    num_str1 = []
    num_str2 = []

#    for i in num_str:
#        if i == num_str[len(num_str)-1]:
#        print(i)
#        #901109
#0 1 2 3 4 5
#0 1 2 3 4
    #print(num)
    for i in range(0, len(num_str)//2 ):
        num_str1.append(num_str[i])
    for i in range(len(num_str)-1, len(num_str)//2 -1, -1):
        num_str2.append(num_str[i])
    for i in range(len(num_str1)):
        #print(num_str1[i]," ",num_str2[i])
        if num_str1[i] == num_str2[i]:
            palindr = True
        else:
            palindr = False
            break
    #print(num_str1,num_str2)
    return palindr
list = []
list2 = []
i = 0
for x in range(900,1000):
    for y in range(900,1000):
        #print("x=",x," y=",y)
        if palindromic(x,y):
            list.append(x*y)
            list2.append(str(x) + " " + str(y))


print(max(list)," and it is ", list2[list.index(max(list))])
#print(palindromic(991,999))
