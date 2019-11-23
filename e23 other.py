#find the sum of all the positive integers that cannot be written as the sum of two abundant numbers

#Every number above 20161 can be written as two abundant numbers

#every multiple of a perfect number is abundant

#every multiple of abundant number is abundant


abun = [12]
no_abun = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for i in range(13, 28123):
    if i in abun or i in no_abun:
        continue
    factors = set()
    factors.add(1)
    for u in range(2, i):
        if u in factors:
            continue
        elif i%u == 0:
            factors.update([u, i/u])
    if sum(factors) > i:
        count = 2
        abun.append(i)
        num = count*i
        while num < 28123:
            abun.append(num)
            count += 1
            num = num*count
    elif sum(factors) == i:
        no_abun.append(i)
        count = 2
        num = count*i
        while num < 28123:
            abun.append(num)
            count += 1
            num = num*count



    else:
        no_abun.append(i)


print(sorted(abun))
print()
print('The length of abun is:', len(abun))
print()
print(no_abun)
print()
print('The length of no_abun is:', len(no_abun))


abun_set = set()

for i, u in enumerate(abun):
    for k in abun[i:]:
        if (u+k) <= 28123:
            abun_set.add(u+k)


nonabun_list = []
for i in range(0, 28123):
    if i not in abun_set:
        nonabun_list.append(i)


print(sum(nonabun_list))