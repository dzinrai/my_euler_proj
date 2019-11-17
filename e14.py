list_collatzs = []
finder = 0
num = 1

while num<=1000000:
    list_collatzs.append(num)
    num_temp = num
    while num_temp > 1:
        if num_temp % 2 == 0:
            num_temp = int(num_temp / 2)
            list_collatzs.append(num_temp)
        else:
            num_temp = int(num_temp * 3 + 1)
            list_collatzs.append(num_temp)

    #print(list_collatzs)
    if len(list_collatzs)>finder:
        finder = len(list_collatzs)
        print(list_collatzs)
        print(finder)

    #i = input()
    list_collatzs = []
    num+=1