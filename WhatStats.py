#V_1.0 by Meghraj Goswami
#***************************************************
import matplotlib.pyplot as plt
import datetime
try:
    fname = input("Enter full path to txt file: ")
    f = open(fname,encoding="utf-8")
    g = open(fname,encoding="utf-8")
except FileNotFoundError:
    print("File not found, try again")
    exit()
dates_list, date_names, user_dict, tot_dates = [], [], {}, {}
#***************************************************
for j in f:
    if j.find(':',13)==-1:
        continue
    try:
        abc=j[j.find('- ')+2:j.find(': '):]
        try:
            a=datetime.datetime.strptime(j[0:j.find(',')], '%m/%d/%y')
        except ValueError:
            a=datetime.datetime.strptime(j[0:j.find(',')], '%d/%m/%y')
        dates_list.append(a.strftime('%b%d,%y'))
        date_names.append(a.strftime('%b%d,%y')+abc)
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
    if i.find(':',13)==-1:
        continue
    try:
        for j in list(user_dict.keys()):
            temp_i=i[i.find('- ')+2:i.find(': '):]
            try:
                date_i=datetime.datetime.strptime(i[0:i.find(',')], '%m/%d/%y')
            except ValueError:
                date_i=datetime.datetime.strptime(i[0:i.find(',')], '%d/%m/%y')
            if temp_i==j:
                z.append(date_i.strftime('%b%d,%y')+j)
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