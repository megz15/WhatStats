#V_1.2 by Meghraj Goswami#

#---Import Libraries Create TK window & Declare Variables---#
from tkinter import * 
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import datetime

root = Tk() 
root.geometry('200x100')

days_not_months = [13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
dates_list, date_names, date_types, d_or_m = [],[],[],[]
tot_ints, user_dict = {},{}

#---Open Text File and create Date Lists---#
def open_file():
    global f
    file = askopenfile(mode='r',filetypes=[('WA Chat Export Text Files','*.txt')],title='Open WhatsApp Chat Export txt file')
    if file is not None:
        f=open(file.name,encoding='utf-8')
        g=open(file.name,encoding='utf-8')
    for l in f:
        if l.find(': ',l.find(':')+1)==-1:
            continue
        else:
            try:
                d_or_m.append(int(l[:2:].replace('-','').replace('/','').replace('.',''))) #Get first two digits to check day or month (>12, not month)
            except ValueError:
                continue
    for k in g:
        if k.find(': ',k.find(':')+1)==-1:
            continue
        else:
            try:
                abc=k[k.find('- ')+2:k.find(': '):]
                q=k[:k.find(', ')]
                if calc_date(q)!=None:
                    dates_list.append(calc_date(q)) #Get dates
                    date_names.append(calc_date(q)+abc) #Get name-date combo
                else:
                    continue
                if abc in list(user_dict.keys()):
                    pass
                else:
                    user_dict[abc]={} #Add members
            except ValueError:
                continue
    for i in list(dict.fromkeys(date_names)):
        for j in list(user_dict.keys()):
            res = [x.isdigit() for x in i[::-1]].index(True) #Find member name from name-date combo
            if j==i[len(i)-res::]:
                for za in list(calc_interval(dates_list).keys()):
                    if i[:len(i)-res:]==za:
                        user_dict[j].update({za:date_names.count(i)}) #Update number of msgs per user for each day
            

#---Plot Graph---#
def plot_graph():
    y=[]
    for i in tot_ints:
        y.append(dates_list.count(i)) #y-ticks (for total messages)
    if (f.name).find("WhatsApp Chat with ")!=-1:
        t0 = (f.name)[(f.name).find("WhatsApp Chat with ")::]
        t0 = t0.replace('Chat with','ChatStats for').rstrip('.txt')
        t0+='\n'
    else:
        t0 = 'WhatStats\n'

    plt.figure('WhatStats')

    plt.axes().xaxis.set_major_locator(tick.MultipleLocator(int(txt_divs.get()))) #x-tick intervals
    plt.axes().xaxis.set_minor_locator(tick.MultipleLocator(1))

    plt.plot(list(tot_ints.keys()),y,label="Total",alpha=0.2) #Plot total messages line chart

    for i in user_dict:
        tot_ints_copy=tot_ints.copy()
        tot_ints_copy.update(user_dict[i]) #Update total messages per user per day
        plt.plot(list(tot_ints_copy.keys()),list(tot_ints_copy.values()),label=i) #Plot messages p/u/p/d
    plt.xticks(rotation=45)
    plt.ylabel('Frequency of messages')
    if len(user_dict)<=10:
        t0+="Members: "+str(list(user_dict.keys())).lstrip('[').rstrip(']').replace("'",'')
        plt.legend()
    else:
        t0+=str(len(user_dict))+' Members in Group'
        plt.legend(ncol=round(len(user_dict)/20),fontsize=8) #For better graph viewing
    plt.title(t0)
    plt.show()

#---Calculate Date Format Automatically---#
def calc_date(o_date):
    if any(x in days_not_months for x in d_or_m):
        date_types=['%d/%m/%y','%d/%m/%Y','%d-%m-%y','%d-%m-%Y','%d.%m.%y','%d.%m.%Y','%d/%m/%y','%d/%m/%Y','%d-%m-%y','%d-%m-%Y','%d.%m.%y','%d.%m.%Y']
    else:
        date_types=['%m/%d/%y','%m/%d/%Y','%m-%d-%y','%m-%d-%Y','%m.%d.%y','%m.%d.%Y','%m/%d/%y','%m/%d/%Y','%m-%d-%y','%m-%d-%Y','%m.%d.%y','%m.%d.%Y']
    for typ in date_types:
        try:
            a=datetime.datetime.strptime(o_date,typ)
            return(a.strftime('%b%d,%y'))
        except ValueError:
            continue

#---Calculate Time Interval---#
def calc_interval(dlist):
    a=datetime.datetime.strptime(dlist[0],'%b%d,%y')
    b=datetime.datetime.strptime(dlist[-1],'%b%d,%y')
    for j in range((b-a).days+1):
        z=(a+datetime.timedelta(days=j))
        tot_ints[z.strftime('%b%d,%y')]=0
    return(tot_ints)

#---Place widgets---#
btn_open = Button(root, text ='Open', command = open_file)
btn_open.place(x=20,y=20)
txt_divs = Entry(root,width=3)
txt_divs.place(x=100,y=22)
btn_plot = Button(root, text ='Plot', command = plot_graph)
btn_plot.place(x=20,y=50)
mainloop()
