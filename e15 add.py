quad1 = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

W = []


for j in range(4):
    W.append(j)

for i in range(4):
    for j in range(1,4):
        W[j] = W[j-1] + W[j]

print(W)

