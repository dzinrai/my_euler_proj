x = 13863300
while True:
    is_found = False
    for y in range(20,0,-1):
        if x % y == 0:
            if y == 1:
                print(x)
                is_found = True
        else:
            break
    if is_found:
        print("FOUNDED = ", x)
        break
    else:
        print(x)
        x+=20