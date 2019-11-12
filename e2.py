x = 4000000
list = [1,2]
list_out = [2]
i1 = 0
i2 = 1
y = sum(list_out)
while y<4000000:
    print("y = ",y)

    x = list[i1]+list[i2]
    list.append(x)
    if x >= 4000000:
        break
    if x%2==0:
        list_out.append(x)

    i1+=1
    i2+=1
    y = sum(list_out)



print("Last = ", list_out)
print(sum(list_out))