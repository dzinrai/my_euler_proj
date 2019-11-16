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
x = 2
list = []
sum = 0

while x<31:
    if funcy(x):
        print(x)
        sum +=x

    x += 1

print(sum)
#142913828912 +10
