import math
def funcy(num):
    prime = True

    for x in range(1,int(math.sqrt(num))+1):
        #print("num=",num,"x=",x)
        if num % 2==0 or num % 3==0 or num % 5==0:
            return False

        if num % x == 0 and x!=num and x!=1:
            #print(num," Not prime")
            return False

    return prime
x = 13
list = []
i = 5
while True:
    if funcy(x):
        i += 1
        print("i= ",i,"num= ",x)
        if i ==10001:
            break
    x+=1

