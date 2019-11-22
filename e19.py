2000
year = [1,2,3,4,5,6,7,8,9,10,11,12]
list_years = []
list_mon = []
visoc = False
for years in range(1900,2001):
    if years % 4 == 0:
        visoc = True
        if years % 100 == 0 and years % 400 != 0:
            visoc = False
    else:
        visoc = False
    list_mon = []
    for month in year:
        if month!=2 and month!=4 and month!=6 and month!=9 and month!=11:
            list_mon.append(31)
        else:
            if month !=2:
                list_mon.append(30)
            else:
                if visoc:
                    list_mon.append(29)
                else:
                    list_mon.append(28)
    list_years.append([years,list_mon])


temp = 0
temp_cal_month = []
names = ['mon','thu','wed','thr','fri','sut','sun']
sunday_counter = 0
print("=============================")
day = 0

for year in list_years:
    #print('{}'.format(year))
    month_count = 0
    temp_cal_month = []
    days_in_months = year[1]
    #print('daysinmonth= ',days_in_months)
    for month in days_in_months:
        temp = month # temp = 31
        #print(temp)
        month_count+=1
        for i in range(0,temp):
            temp_cal_month.append([month_count,i+1,names[day]])
            if day<6:
                day+=1
            else:
                if i<temp:
                    day=0
        #print(temp_cal_month)
    year[1] = temp_cal_month
    print('{} = {}'.format(year[0], year[1]))
print("=============================")
list_years.pop(0)
for year in list_years:
    for day in year[1]:
        if day[2] == 'sun' and day[1] == 1:
            sunday_counter+=1
            print('year = {} day {}'.format(year[0], day))
print(sunday_counter)








