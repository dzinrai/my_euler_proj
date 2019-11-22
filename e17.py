
list_words = []
patterns = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
patterns_ty = ['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
patterns_hundreds = ['hundred','hundreds']
num_str = ''
def paterns(num):
    if num >= 1 and num<20:
        return patterns[num]
    else:
        return patern_doub(num)


def patern_doub(num):
    i = num // 10
    j = num % 10
    return patterns_ty[i - 1] + " " + patterns[j]
demon_num = ""
counter = 0
for x in range(1,1001):
    i=0
    j=0
    if x<100:
        num_str = paterns(x)

    if x>=100 and x<1000:
        i = x//100
        j = x % 100
        if j == 0:
            num_str = paterns(i) + " " + patterns_hundreds[0]
        else:
            num_str = paterns(i) + " " + patterns_hundreds[0] + " and " + paterns(j)
    if x==1000:
        num_str = 'one thousand'
    counter += len(num_str.replace(" ", ''))
    demon_num += num_str.replace(" ","")
    print('{}                   x={} i={} j={} len={} c={}'.format(num_str,x,i,j,len(num_str.replace(" ", '')),counter))
    #print(paterns(j))

    num_str = ''
print(counter)
print(demon_num)
print(len(demon_num))
