
a=1
b=2
c=3
list = [a,b,c]
lister = []
def checks(a,b,c):
    global lister
    #print("a=", a, "b=", b, "c=", c)
    if a + b + c == 1000:
        if c ** 2 == a ** 2 + b ** 2:
            print("OMEGALUL a=",a,"b=",b)
            lister.append(a)
            lister.append(b)
            lister.append(c)
            return True
    return False

for xc in range(3,1000):
    if len(lister) > 0:
        break
    c = xc
    #checks(a,b,xc)
    print("                             c= ",xc)
    for xb in range(2,xc):
        b = xb
        if len(lister)>0:
            break

        print("                             c= ", xc)
        print("                 b= ",xb)
        print("      a= ", a)
        #checks(a, xb, xc)
        for xa in range(1,xb):
            a = xa
            if len(lister) > 0 or xa >= xb:
                break
            else:
                if xa + xb + xc != 1000:
                    continue
            checks(xa, xb, xc)
            print(xa,xb,xc)

print(lister)
