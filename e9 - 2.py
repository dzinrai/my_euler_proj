a = 1
b = 2
c = 3
list = []
for xc in range(997,2,-1):
    print(xc)
    if xc + b + a == 1000:
        list.append([a, b, xc])
        #print(xc,b,a)
    for xb in range(xc,1,-1):
        if xc + xb + a == 1000:
            list.append([a, xb, xc])
            #print(xc, xb, a)
        for xa in range(xb, 0, -1):
            if xc + xb + xa == 1000:
                list.append([xa, xb, xc])
                #print(xc, xb, xa)

print(list)
for x in list:
    if x[2]