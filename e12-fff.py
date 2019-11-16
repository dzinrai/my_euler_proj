import math
import pickle

f_file = 'trianles.data'
f = open(f_file,'rb')
finder = []
finder = pickle.load(f)
print(finder)
print(len(finder))

for j in [17907120,76576500]:
    ix = 0
    for x in range(1, j + 1):
        if j % x == 0:
            ix += 1
            print('Число {} делится на {} (делитель №{})'.format(j, x, ix))
        if ix > 500 and j % x == 0:
            ix += 1
            print('Число {} делится на {} (делитель №{})'.format(j, x, ix))
            break


