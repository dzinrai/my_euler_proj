
f_name = 'names.txt'

f = open(f_name)
names = ""
while True:
    line = f.readline()
    if len(line)==0:
        break
    names += line
names = names.replace('"','')
lister = names.split(",")

print(names)
print(lister)
f.close()

def qsort(lst):
    if len(lst)<2:
        return lst
    else:
        pivot = lst[0]

        less = [i for i in lst[1:] if i<=pivot]
        greater = [i for i in lst[1:] if i>pivot]
        return qsort(less) + [pivot] + qsort(greater)

lister = qsort(lister)
print(lister)

orders = "A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-W-X-Y-Z"
orders = orders.split("-")
print(orders)
total_points = 0
for name in lister:
    points = 0
    for x in name:
        points +=  orders.index(x) + 1
    points = (lister.index(name) + 1) * (points)
    lister[lister.index(name)] = [name,points]
    total_points+=points
print(lister)
print(lister[937])
print(total_points)