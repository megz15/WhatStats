#V_1.0 by Meghraj Goswami
#***************************************************
import matplotlib.pyplot as plt
import datetime
try:
    fname = input("Enter full path to txt file: ")
    f = open(fname,encoding="utf-8")
    g = open(fname,encoding="utf-8")
    h = open(fname,encoding="utf-8")
except FileNotFoundError:
    print("File not found, try again")
    exit()
dates_list, date_names, date_types , user_dict, tot_dates, test_lst = [], [], [], {}, {}, []
#***************************************************
days_not_months=[13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
for l in h:
    if l.find(':',17)==-1:
        continue
    try:
        test_lst.append(int(l[0:l.find('/')]))
    except ValueError:
        continue

for i in days_not_months:
    if i in test_lst:
        date_types=['%d/%m/%y','%d/%m/%Y']
    else:
        date_types=['%m/%d/%y','%m/%d/%Y']

def find_date(o_date):
    for typ in date_types:
        try:
            a=datetime.datetime.strptime(o_date,typ).date()
            return a.strftime('%b%d,%y')
        except ValueError:
            pass

for j in f:
    if j.find(':',17)==-1:
        continue
    try:
        abc=j[j.find('- ')+2:j.find(': '):]
        a=j[0:j.find(',')]
        if find_date(a)!=None:
            dates_list.append(find_date(a))
            date_names.append(find_date(a)+abc)
        else:
            continue
        if abc in list(user_dict.keys()):
            pass
        else:
            user_dict[abc]={}
    except ValueError:
        continue
#***************************************************
fdate = datetime.datetime.strptime(dates_list[0],'%b%d,%y')
ldate = datetime.datetime.strptime(dates_list[-1],'%b%d,%y')
diff = ldate - fdate
for i in range(diff.days + 1):
    day=(fdate + datetime.timedelta(days=i))
    tot_dates[day.strftime('%b%d,%y')]=0
#***************************************************
z=[]
for i in g:
    if i.find(':',17)==-1:
        continue
    try:
        for j in list(user_dict.keys()):
            temp_i=i[i.find('- ')+2:i.find(': '):]
            date_i=i[0:i.find(',')]
            if temp_i==j:
                z.append(find_date(date_i)+j)
    except ValueError:
        continue
for i in list(dict.fromkeys(z)):
    for j in list(user_dict.keys()):
        res = [x.isdigit() for x in i[::-1]].index(True)
        if j==i[len(i)-res::]:
            for za in list(tot_dates.keys()):
                if i[:len(i)-res:]==za:
                    user_dict[j].update({za:date_names.count(i)})
#***************************************************
y=[]
for i in tot_dates:
    y.append(dates_list.count(i))
if (f.name).find("WhatsApp Chat with ")!=-1:
    t0 = (f.name)[(f.name).find("WhatsApp Chat with ")::]
    t0 = t0.replace('Chat with','ChatStats for').rstrip('.txt')
    t0+='\n'+"Members: "+str(list(user_dict.keys())).lstrip('[').rstrip(']').replace("'",'')
else:
    t0="Members: "+str(list(user_dict.keys())).lstrip('[').rstrip(']').replace("'",'')
plt.figure('WhatStats')
plt.plot(list(tot_dates.keys()),y,label="Total",alpha=0.2)
for i in user_dict:
    tot_dates_copy=tot_dates.copy()
    tot_dates_copy.update(user_dict[i])
    plt.plot(list(tot_dates_copy.keys()),list(tot_dates_copy.values()),label=i)
plt.xticks(rotation=45)
plt.ylabel('Frequency of messages')
plt.title(t0)
plt.legend()
plt.show()
