import pickle
import time
izb = []
t = time.time()
s = 12

while s < 1:
    temp = 0
    dels = []
    for x in range(1,s):
        if s % x == 0:
            temp += x
            dels.append(x)
    if temp > s:
        izb.append(s)
        print(s,"=",dels)
    s +=1
f = open("izb.data",'rb')

izb2 = pickle.load(f)
f.close()
izb3 = izb2
def worth_list(izb, elem):
    for x in izb:
        if x >= elem:
            i = izb.index(x)
            return izb[0:i]
    return []

z = 1
summ = 0
alt_izb = []

for x in range(1,20162):
    #print("x=",x)
    summ_of_redund = False
    isb_temp = worth_list(izb2, x)
    #print("isb_temp =", isb_temp)
    temp = 0
    for z in isb_temp:
        temp = x-z
        if temp >=0 and temp%2==0 and temp in isb_temp:
            summ_of_redund = True
            print("temp=", temp)
            gl = isb_temp.index(temp) - 10
            print(isb_temp[gl:])
            print("z = ", z)
            break
    if not summ_of_redund:
        summ += x
        alt_izb.append(x)
        #input()
    print('x={} summ={} '.format(x, summ))
    if x % 1000 == 0:
        print(x)
        print(alt_izb)
        print(summ)
        print(sum(alt_izb))
print(summ)

print(time.time() - t)
