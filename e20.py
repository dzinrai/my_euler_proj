import math
num = math.factorial(100)
num = str(num)
ssum = 0
for x in num:
    ssum += int(x)
print(ssum)