#V_2.0 by Meghraj Goswami#

#---Import Libraries Create TK window & Declare Variables---#
from tkinter import * 
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import datetime

root = Tk()
root.title('WECA')
root.geometry('200x170')

days_not_months = [13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
dates_list, date_names, date_types, d_or_m = [],[],[],[]
tot_ints, new_tot_ints, user_dict = {},{},{}

#---Open Text File and create Date Lists---#
def open_file():
    dates_list.clear()
    date_names.clear()
    d_or_m.clear()
    tot_ints.clear()
    user_dict.clear()
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
    range_start['values']=list(tot_ints.keys())
            

#---Plot Graph---#
def plot_graph():
    tot_ints=new_tot_ints
    plt.close('all')
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
    
    tot_ints_list=list(tot_ints.keys())
    for i in user_dict:
        tot_ints_copy=tot_ints.copy()
        tot_ints_copy.update(user_dict[i]) #Update total messages per user per day
        for key in list(tot_ints_copy.keys()):
            if key not in tot_ints_list:
                del tot_ints_copy[key] #Remove extra keys
        plt.plot(list(tot_ints_copy.keys()),list(tot_ints_copy.values()),label=i) #Plot messages p/u/p/d
    plt.xticks(rotation=45)
    plt.ylabel('Frequency of messages')
    if len(user_dict)<=10:
        t0+="Members: "+str(list(user_dict.keys())).lstrip('[').rstrip(']').replace("'",'')
        plt.legend()
    else:
        t0+=str(len(user_dict))+' Members in Group'
        plt.legend(ncol=3,fontsize=8) #For better graph viewing
    plt.title(t0)
    plt.show()
    tot_ints.clear()

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
    tot_ints.clear()
    a=datetime.datetime.strptime(dlist[0],'%b%d,%y')
    b=datetime.datetime.strptime(dlist[-1],'%b%d,%y')
    for j in range((b-a).days+1):
        z=(a+datetime.timedelta(days=j))
        tot_ints[z.strftime('%b%d,%y')]=0
    return(tot_ints)

#---End Range of ComboBox---#
def setEndRange(self):
    a=list(tot_ints.keys()).index(range_start.get())
    range_end['values']=list(tot_ints.keys())[a:]
    
#---Get Ints from Combobox---#
def getTotInts(self):
    new_tot_ints.clear()
    a,b=datetime.datetime.strptime(range_start.get(),'%b%d,%y'),datetime.datetime.strptime(range_end.get(),'%b%d,%y')
    for j in range((b-a).days+1):
        z=(a+datetime.timedelta(days=j))
        new_tot_ints[z.strftime('%b%d,%y')]=0

#---Place widgets---#
btn_open = Button(root, text = 'Open Chat', command = open_file)
btn_open.place(x=62,y=10)
lbl_divs = Label(root, text = 'Enter interval b/w dates: ')
lbl_divs.place(x=10,y=42)
txt_divs = Entry(root,width=6)
txt_divs.place(x=150,y=40)
range_frame = LabelFrame(root,text='Select date range')
range_start = Combobox(range_frame,state='readonly',width=8)
range_start.bind('<<ComboboxSelected>>',setEndRange)
lbl_to = Label(range_frame,text='to')
range_end = Combobox(range_frame,state='readonly',width=8)
range_end.bind('<<ComboboxSelected>>',getTotInts)
range_frame.place(x=10,y=70)
range_start.grid(row=0,column=0,padx=5,pady=5)
lbl_to.grid(row=0,column=1,padx=5,pady=5)
range_end.grid(row=0,column=2,padx=5,pady=5)
btn_plot = Button(root, text = 'Plot Graph!', command = plot_graph)
btn_plot.place(x=62,y=130)
mainloop()
