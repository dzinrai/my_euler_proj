import math
import pickle
num = 1
list = []
Ssum = 0
list_triangles = []
finder = 0
fnd = []
list_finders = []


temp_fff = []

while True:
    #print(num)
    list.append(num)
    Ssum = sum(list)
    list_triangles.append(Ssum)
    #print(Ssum)
    i = 1
    index_del = 0
    for x in range(1,int(math.sqrt(Ssum)+1)):
        #print("          Ssum = ", Ssum)
        #print("x = ", x)
        if Ssum % x == 0:
            index_del += 1
        if index_del > 500:

            finder = Ssum
            break

    #[[205761, 8],[205761, 8]]

    if len(list_finders) == 0:
        list_finders = [Ssum, index_del]
    else:
        if list_finders[1] < index_del:
            list_finders = [Ssum, index_del]
            print(list_finders)
    if finder != 0:
        print("====================OMEGALUL = ",fnd)
        temp_fff = list_triangles
        print(temp_fff)
        print("------------", len(temp_fff))
        #842161320
        temp_fff = list_triangles

        #f_file = 'trianles.data'

        temp_fff.reverse()

        #f = open(f_file,'wb')
        #pickle.dump(temp_fff,f)
        #f.close()

        for j in temp_fff:
            ix = 0
            for x in range(1,j+1):
                if j % x == 0:
                    ix += 1
                if ix > 500 and j % x == 0:
                    ix += 1
                    print('num={} dels={}'.format(j,ix))
        #break
    num+=1
