from collections import deque
import pickle
string_f = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

rows = []

lines = string_f.split('\n')
for string in lines:
    rows.append(string.split(' '))
rows_main = []
i = 0
for num_str_list in rows:
    rows_main.append([])
    for x in num_str_list:
        rows_main[i].append(int(x))
    i+=1

graph = {}

for x in rows_main:
    index_x = rows_main.index(x)
    for y in x:
        index_y = x.index(y)
        if index_x+1 < len(rows_main):
            try:
                graph[y, index_x, index_y] += [ (rows_main[index_x + 1][index_y],index_x+1, index_y), (rows_main[index_x + 1][index_y + 1],index_x +1, index_y+1) ]
            except KeyError:
                graph[y, index_x, index_y] = [ (rows_main[index_x + 1][index_y],index_x+1, index_y), (rows_main[index_x + 1][index_y + 1],index_x+1, index_y+1) ]
            else:
                pass

print(graph)


def find_all_paths(graph, start, end, path=[]):
    input()
    print('start ={} end={}'.format(start,end))
    path = path + [start]
    if start == end:
        print('{}=={} -> paths={}'.format(start, end, path))
        return [path]
    if not start in graph:
        print('{} такого нет в графе'.format(start))
        return []
    paths = []
    print('paths={}'.format(paths))
    for node in graph[start]:
        #input()
        #print('node=',node)
        if node not in path:
            print('{} node not in path {}'.format(node,path))
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
s = 0
i = 0
summ = 0
for x in rows_main[-1]:
    print((x,14,i))
    paths = find_all_paths(graph,(75,0,0),(x,14,i))
    k = 0
    for z in paths:
        print(k," = ",z)
        k+=1
    s += len(paths)
    i += 1
    for zs in paths:
        temp_summ = 0
        for xs in zs:
            temp_summ += xs[0]
        if temp_summ > summ:
            summ = temp_summ
    #input()
print(s)


print(summ)
'''
paths = []
temp = []

for x,y in graph.items():
    print('selected={}->{} selected={}->{}'.format(x,y[0],x,y[1]))
    input()
    for z in paths:
        print('x={} paths={} z={}'.format(x,paths,z))
        input()
        if z[-1] == x:
            print('{} removed'.format(z))
            temp = z
            paths.remove(z)
    if len(temp)>0:
        paths.append(temp + [y[0]])
        paths.append(temp + [y[1]])
    else:
        paths.append(temp + [x, y[0]])
        paths.append(temp + [x, y[1]])
    print('paths={}'.format(paths))



f=open('paths.data','wb')

pickle.dump(paths, f)# помещаем объект в файлf.close()

print('Paths len = ',len(paths))

sum = 0
for x in paths:
    temp_sum = 0
    for y in x:
        temp_sum += y[0]
    if temp_sum>sum:
        sum = temp_sum
        print(sum)

'''


