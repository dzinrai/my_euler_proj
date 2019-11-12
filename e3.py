c = 600851475143
def funcy(num):
    prime = True
    for x in range(1,num+1):
        #print("num=",num,"x=",x)
        if num % x == 0 and x!=num and x!=1:
            #print(num," Not prime")
            prime = False
            break

    return prime


#funcy(c)
#print("Prime? ",funcy(600851475143))
x=2
list = []
while x < c+1:
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
        x += 1
        continue
    #print(x)
    if funcy(x):
        if c % x == 0:
            list.append(x)
            print(list)
    x+=1
