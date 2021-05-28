"""
Developed By Samarth Anand
"""
import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import pandas as pd

df = pd.read_csv("attendance.csv")

import calendar

import warnings
warnings.filterwarnings("ignore")

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family {Comic Sans MS} -size 24 -weight bold"
        font13 = "-family {Comic Sans MS} -size 20 -weight bold"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font=font13)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        self.style.configure("Heading", font="-family {Comic Sans MS} -size 14 ", background="#d9d9d9")
        self.style.configure(".", font="-family {Comic Sans MS} -size 12 ")
        # style1.map('.', background=[('selected', _compcolor)])#, ('active', _ana2color)])
        self.style.map('Treeview', background=[('background', '#d9d9d9'), ('selected', "blue")])

        top.geometry("1162x715+200+100")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Attendance Register")
        top.configure(background="#d9d9d9")
        top.protocol('WM_DELETE_WINDOW', sam)

        global year1, month1, value, option
        year1 = tk.StringVar()
        month1 = tk.StringVar()
        value = tk.StringVar()
        option = tk.StringVar()

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.012, relwidth=1.0)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#BCE7FA")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.342, rely=0.012, height=66, width=418)
        self.Label1.configure(background="#BCE7FA")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Attendance Register''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.018, rely=0.182, height=37, width=216)
        self.Label2.configure(background="#BCE7FA")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font13)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Enter Year''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.027, rely=0.279, height=56, width=212)
        self.Label3.configure(background="#BCE7FA")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font13)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Enter Month''')

        self.Entry1 = tk.Entry(self.Frame1, textvariable=year1)
        self.Entry1.place(relx=0.261, rely=0.158,height=65, relwidth=0.237)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font13)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2 = tk.Entry(self.Frame1, textvariable=month1)
        self.Entry2.place(relx=0.261, rely=0.267,height=65, relwidth=0.237)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font=font13)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.027, rely=0.4, height=47, width=197)
        self.Label4.configure(background="#BCE7FA")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font13)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Category''')

        self.TCombobox1 = ttk.Combobox(self.Frame1, textvariable=option, state='readonly')
        value_list = ['Id', 'Name', 'Branch', 'Designation', 'Email']
        self.TCombobox1.place(relx=0.261, rely=0.376, relheight=0.081
                , relwidth=0.237)
        self.TCombobox1.configure(values=value_list)
        self.TCombobox1.configure(font=font13)
        self.TCombobox1.configure(takefocus="")
        option.set("Choose Category")

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.054, rely=0.497, height=47, width=131)
        self.Label5.configure(background="#BCE7FA")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font13)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Value''')

        self.Entry3 = tk.Entry(self.Frame1, textvariable=value)
        self.Entry3.place(relx=0.261, rely=0.485,height=64, relwidth=0.237)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font=font13)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Button1 = tk.Button(self.Frame1, command=clear_page1)
        self.Button1.place(relx=0.045, rely=0.642, height=62, width=216)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#568EF9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font13)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Clear''')

        self.Button2 = tk.Button(self.Frame1, command=page1_calc)
        self.Button2.place(relx=0.306, rely=0.642, height=62, width=216)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#568EF9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Comic Sans MS} -size 20 -weight bold")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Find''')

        self.Button3 = tk.Button(self.Frame1, command=sam)
        self.Button3.place(relx=0.045, rely=0.776, height=63, width=216)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#568EF9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font="-family {Comic Sans MS} -size 20 -weight bold")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Exit''')

        self.Button4 = tk.Button(self.Frame1, command=page1_to_2)
        self.Button4.place(relx=0.306, rely=0.776, height=62, width=216)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#568EF9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font="-family {Comic Sans MS} -size 20 -weight bold")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Next''')

        # self.Text1 = tk.Text(self.Frame1)
        # self.Text1.place(relx=0.531, rely=0.121, relheight=0.841, relwidth=0.443)
        #
        # self.Text1.configure(background="white")
        # self.Text1.configure(font="TkTextFont")
        # self.Text1.configure(foreground="black")
        # self.Text1.configure(highlightbackground="#d9d9d9")
        # self.Text1.configure(highlightcolor="black")
        # self.Text1.configure(insertbackground="black")
        # self.Text1.configure(selectbackground="#c4c4c4")
        # self.Text1.configure(selectforeground="black")
        # self.Text1.configure(wrap="word")

        global listBox
        cols = ('Id', 'Name', 'Attendance')
        listBox = ttk.Treeview(self.Frame1, columns=cols, show='headings', selectmode='browse')
        for col in cols:
            listBox.heading(col, text=col)
            if(col=="Name"):
                listBox.column(col, minwidth=0, width=200)
            elif(col=="Id"):
                listBox.column(col, minwidth=0, width=10)
            else:
                listBox.column(col, minwidth=0, width=50)
        listBox.place(relx=0.531, rely=0.121, relheight=0.841, relwidth=0.443)


class Toplevel2:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Comic Sans MS} -size 20 -weight bold"
        font11 = "-family {Segoe UI} -size 20 -weight bold"
        font12 = "-family {Comic Sans MS} -size 18 -weight bold"
        font13 = "-family {Comic Sans MS} -size 16 -weight bold"
        font9 = "-family {Comic Sans MS} -size 24 -weight bold"

        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font=font13)
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        top.geometry("1162x735+200+90")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Attendance Register")
        top.configure(background="#d9d9d9")
        top.protocol('WM_DELETE_WINDOW', sam)

        self.style.configure("Heading", font="-family {Comic Sans MS} -size 14 ", background="#d9d9d9")
        self.style.configure(".", font="-family {Comic Sans MS} -size 12 ")
        # style1.map('.', background=[('selected', _compcolor)])#, ('active', _ana2color)])
        self.style.map('Treeview', background=[('background', '#d9d9d9'), ('selected', "blue")])

        global year2, month2, id, name, branch, designation
        year2 = tk.StringVar()
        month2 = tk.StringVar()
        id = tk.StringVar()
        name = tk.StringVar()
        branch = tk.StringVar()
        designation = tk.StringVar()

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.005, relwidth=1.001)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#BCE7FA")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.331, rely=0.008, height=54, width=451)
        self.Label1.configure(background="#BCE7FA")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Attendance Register''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.036, rely=0.138, height=55, width=203)
        self.Label2.configure(background="#BCE7FA")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Enter Year''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.029, rely=0.238, height=55, width=225)
        self.Label3.configure(background="#BCE7FA")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font10)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Enter Month''')

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.009, rely=0.338, height=46, width=283)
        self.Label4.configure(background="#BCE7FA")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font11)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Enter Person Id''')

        self.Entry1 = tk.Entry(self.Frame1, textvariable=year2)
        self.Entry1.place(relx=0.224, rely=0.125,height=63, relwidth=0.219)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2 = tk.Entry(self.Frame1, textvariable=month2)
        self.Entry2.place(relx=0.224, rely=0.225,height=63, relwidth=0.219)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="-family {Comic Sans MS} -size 20 -weight bold")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.Entry3 = tk.Entry(self.Frame1, textvariable=id)
        self.Entry3.place(relx=0.224, rely=0.325,height=62, relwidth=0.219)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="-family {Comic Sans MS} -size 20 -weight bold")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")

        self.Button1 = tk.Button(self.Frame1, command=clear_page2)
        self.Button1.place(relx=0.036, rely=0.463, height=70, width=235)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#568EF9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font10)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Clear''')

        self.Button2 = tk.Button(self.Frame1, command=page2_calc)
        self.Button2.place(relx=0.253, rely=0.463, height=70, width=236)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#568EF9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Comic Sans MS} -size 20 -weight bold")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Find''')

        self.Button3 = tk.Button(self.Frame1, command=page2_to_1)
        self.Button3.place(relx=0.036, rely=0.588, height=70, width=235)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#568EF9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font="-family {Comic Sans MS} -size 20 -weight bold")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Back''')

        self.Button4 = tk.Button(self.Frame1, command=sam)
        self.Button4.place(relx=0.253, rely=0.588, height=70, width=236)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#568EF9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font="-family {Comic Sans MS} -size 20 -weight bold")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Exit''')

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.029, rely=0.726, height=54, width=233)
        self.Label5.configure(background="#BCE7FA")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font12)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Name''')

        self.Label6 = tk.Label(self.Frame1)
        self.Label6.place(relx=0.029, rely=0.814, height=56, width=233)
        self.Label6.configure(background="#BCE7FA")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font12)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Branch''')

        self.Label7 = tk.Label(self.Frame1)
        self.Label7.place(relx=0.029, rely=0.901, height=55, width=233)
        self.Label7.configure(background="#BCE7FA")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font=font10)
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Designation''')

        self.Entry4 = tk.Entry(self.Frame1, state='readonly', textvariable=name)
        self.Entry4.place(relx=0.217, rely=0.726,height=54, relwidth=0.234)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font=font13)
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")

        self.Entry5 = tk.Entry(self.Frame1, state='readonly', textvariable=branch)
        self.Entry5.place(relx=0.217, rely=0.814,height=55, relwidth=0.234)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font=font13)
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")

        self.Entry6 = tk.Entry(self.Frame1, state='readonly', textvariable=designation)
        self.Entry6.place(relx=0.217, rely=0.901,height=54, relwidth=0.234)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font=font13)
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(insertbackground="black")

        # self.Text1 = tk.Text(self.Frame1)
        # self.Text1.place(relx=0.505, rely=0.113, relheight=0.846, relwidth=0.472)
        #
        # self.Text1.configure(background="white")
        # self.Text1.configure(font="TkTextFont")
        # self.Text1.configure(foreground="black")
        # self.Text1.configure(highlightbackground="#d9d9d9")
        # self.Text1.configure(highlightcolor="black")
        # self.Text1.configure(insertbackground="black")
        # self.Text1.configure(selectbackground="#c4c4c4")
        # self.Text1.configure(selectforeground="black")
        # self.Text1.configure(wrap="word")

        global listBox2
        cols1 = ('Date', 'Arrival Timming', 'Departure Timming')
        listBox2 = ttk.Treeview(self.Frame1, columns=cols1, show='headings', selectmode='browse')
        for col in cols1:
            listBox2.heading(col, text=col)
            if (col == "Date"):
                listBox2.column(col, minwidth=0, width=50)
            else:
                listBox2.column(col, minwidth=0, width=100)
        listBox2.place(relx=0.505, rely=0.083, relheight=0.90, relwidth=0.472)


def page1_calc():
    listBox.delete(*listBox.get_children())
    y=year1.get()
    if(len(y)==4):
        y=y[2:]
    m=month1.get()
    if(len(m)==1):
        m='0'+m
    m2=str(int(m)+1)
    if(len(m2)==1):
        m2="0"+m2

    date1=m+"-01-"+y
    date2 = m2+"-01-"+y
    q1='date>"'+date1+'" and date<"'+date2+'"'



    file = df.query(q1)

    a = value.get()
    b1=option.get()
    if(b1=="Id"):
        category="Id"
        a=int(a)
    elif(b1=="Name"):
        category="name"
    elif (b1 == "Branch"):
        category = "branch"
    elif(b1 == "Designation"):
        category = "designation"
    elif(b1=="Email"):
        category="email"


    ids = file[file[category] == a]["Id"]
    for i in ids.unique():
        sam = file[file["Id"] == i][["date", "name"]]
        listBox.insert("", "end", values=(i, sam["name"].unique()[0],len(sam["date"].unique())))


def page2_calc():
    listBox2.delete(*listBox2.get_children())
    y = year2.get()
    m = month2.get()
    identity = id.get()


    if (len(y) == 4):
        y = y[2:]

    if (len(m) == 1):
        m = '0' + m

    m2 = str(int(m) + 1)
    if (len(m2) == 1):
        m2 = "0" + m2


    date1 = m + "-01-" + y
    date2 = m2 + "-01-" + y


    q1='date>"'+date1+'" and date<"'+date2+'" and Id=='+identity
    print(q1)
    x = df.query(q1)
    print(x)

    sunday = [i[6] for i in calendar.monthcalendar(int("20"+y),int(m)) if i[6] != 0]
    days=calendar.monthrange(int("20"+y),int(m))

    b = x["date"].tolist()

    name.set(df[df["Id"]==int(identity)]["name"].unique()[0])
    branch.set(df[df["Id"]==int(identity)]["branch"].unique()[0])
    designation.set(df[df["Id"]==int(identity)]["designation"].unique()[0])

    for i in range(1, days[1]+1):
        if (i < 10):
            date = m+"-0" + str(i) + "-20"+y
        else:
            date = m+"-" + str(i) + "-20"+y

        z = x[(x['Id'] == int(identity)) & (x['date'] == date)]['time'].tolist()

        if (b.count(date) == 1):
            ari_timing =z[0]
            dep_timing = "Not Available"

        elif(i in sunday and b.count(date) > 0):
            z.sort()
            ari_timing = z[0]
            dep_timing = z[-1]

        elif(i in sunday):
            ari_timing = "Sunday"
            dep_timing = "Sunday"

        elif(b.count(date) == 0):
            ari_timing = "Absent"
            dep_timing = "Not Available"
        else:
            z.sort()
            ari_timing = z[0]
            dep_timing = z[-1]
        listBox2.insert("", "end", values=(date, ari_timing, dep_timing))





def sam():
    root.destroy()

def page1_to_2():
    page2.deiconify()
    page1.withdraw()

def page2_to_1():
    page1.deiconify()
    page2.withdraw()


def clear_page1():
    year1.set("")
    month1.set("")
    value.set("")
    option.set("Choose Category")

def clear_page2():
    year2.set("")
    month2.set("")
    id.set("")

if __name__ == '__main__':
    root = tk.Tk()
    page1 = tk.Toplevel(root)
    page2 = tk.Toplevel(root)
    Toplevel1(page1)
    Toplevel2(page2)
    root.withdraw()
    page2.withdraw()
    root.mainloop()





