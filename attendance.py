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

from sqlite3 import *
conn = connect('record_form.db')
mycursor = conn.cursor()

try:
    mycursor.execute('select * from record limit 1')
except(OperationalError):
    mycursor.execute("create table record(rec_id text, name text, branch text, profession text, email text)")


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 18 -weight bold"
        font12 = "-family {Segoe UI} -size 16 -weight bold"
        font13 = "-family {Courier New} -size 16 -weight bold"
        font15 = "-family {Segoe UI} -size 13 -weight bold"
        font9 = "-family {Segoe UI} -size 22 -weight bold"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])


        self.style.configure("Heading", font="-family {Comic Sans MS} -size 14 ", background="#d9d9d9")
        self.style.configure(".", font="-family {Comic Sans MS} -size 12 ")
        # style1.map('.', background=[('selected', _compcolor)])#, ('active', _ana2color)])
        self.style.map('Treeview', background=[('background', '#d9d9d9'), ('selected', "blue")])

        top.geometry("1448x800+0+0")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.protocol('WM_DELETE_WINDOW', sam)

        global id, name, branch, designation, email, option, value
        id = tk.StringVar()
        name = tk.StringVar()
        branch = tk.StringVar()
        designation = tk.StringVar()
        email = tk.StringVar()
        option = tk.StringVar()
        value = tk.StringVar()


        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.004, relwidth=1.005)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#acffff")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.328, rely=0.024, height=48, width=592)
        self.Label1.configure(background="#acffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#0000ff")
        self.Label1.configure(text='''Attendance Monitoring System''')

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.026, rely=0.118, relheight=0.833, relwidth=0.46)

        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#acffff")
        self.Frame2.configure(highlightcolor="#8000ff")

        self.Label2 = tk.Label(self.Frame2)
        self.Label2.place(relx=0.265, rely=0.014, height=36, width=332)
        self.Label2.configure(background="#acffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#0000a0")
        self.Label2.configure(text='''Add / Delete Record''')

        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.033, rely=0.099, height=36, width=55)
        self.Label3.configure(background="#acffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font12)
        self.Label3.configure(foreground="#8080ff")
        self.Label3.configure(text='''Id''')

        self.Entry1 = tk.Entry(self.Frame2,textvariable=id)
        self.Entry1.place(relx=0.126, rely=0.099,height=54, relwidth=0.187)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font13)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label4 = tk.Label(self.Frame2)
        self.Label4.place(relx=0.349, rely=0.114, height=45, width=112)
        self.Label4.configure(background="#acffff")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font12)
        self.Label4.configure(foreground="#8080ff")
        self.Label4.configure(text='''Name''')

        self.Entry2 = tk.Entry(self.Frame2,textvariable=name)
        self.Entry2.place(relx=0.517, rely=0.099,height=54, relwidth=0.439)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font=font13)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Label5 = tk.Label(self.Frame2)
        self.Label5.place(relx=0.028, rely=0.199, height=46, width=112)
        self.Label5.configure(background="#acffff")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font12)
        self.Label5.configure(foreground="#8080ff")
        self.Label5.configure(text='''Branch''')

        self.Entry3 = tk.Entry(self.Frame2,textvariable=branch)
        self.Entry3.place(relx=0.209, rely=0.199,height=54, relwidth=0.201)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font=font13)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Label6 = tk.Label(self.Frame2)
        self.Label6.place(relx=0.447, rely=0.199, height=46, width=182)
        self.Label6.configure(background="#acffff")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font12)
        self.Label6.configure(foreground="#8080ff")
        self.Label6.configure(text='''Designation''')

        self.Entry4 = tk.Entry(self.Frame2,textvariable=designation)
        self.Entry4.place(relx=0.712, rely=0.199,height=54, relwidth=0.257)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font=font13)
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")

        self.Entry5 = tk.Entry(self.Frame2,textvariable=email)
        self.Entry5.place(relx=0.209, rely=0.298,height=54, relwidth=0.76)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font=font13)
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")

        self.Label7 = tk.Label(self.Frame2)
        self.Label7.place(relx=0.014, rely=0.298, height=46, width=112)
        self.Label7.configure(background="#acffff")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font=font12)
        self.Label7.configure(foreground="#8080ff")
        self.Label7.configure(text='''Email''')

        self.Button1 = tk.Button(self.Frame2, command=clear_frame1)
        self.Button1.place(relx=0.028, rely=0.412, height=53, width=196)
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(font=font12)
        self.Button1.configure(foreground="#0000a0")
        self.Button1.configure(text='''Clear''')

        self.Button2 = tk.Button(self.Frame2, command=save_record)
        self.Button2.place(relx=0.349, rely=0.412, height=53, width=196)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font12)
        self.Button2.configure(foreground="#0000a0")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Save''')

        self.Button3 = tk.Button(self.Frame2, command=delete_record)
        self.Button3.place(relx=0.67, rely=0.412, height=53, width=196)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font=font12)
        self.Button3.configure(foreground="#0000a0")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Delete''')

        # self.Text1 = tk.Text(self.Frame2)
        # self.Text1.place(relx=0.028, rely=0.526, relheight=0.46, relwidth=0.941)
        # self.Text1.configure(background="white")
        # self.Text1.configure(font="TkTextFont")
        # self.Text1.configure(foreground="black")
        # self.Text1.configure(highlightbackground="#d9d9d9")
        # self.Text1.configure(highlightcolor="black")
        # self.Text1.configure(insertbackground="black")
        # self.Text1.configure(selectbackground="#c4c4c4")
        # self.Text1.configure(selectforeground="black")
        # self.Text1.configure(wrap="word")

        global listBox1
        cols = ('Id','Name','Branch','Designation','Email')
        listBox1 = ttk.Treeview(self.Frame2, columns=cols, show='headings', selectmode='browse')
        for col in cols:
            listBox1.heading(col, text=col)
        listBox1.place(relx=0.028, rely=0.526, relheight=0.46, relwidth=0.941)
        # scrollbar = ttk.Scrollbar(orient=tk.HORIZONTAL, command=ttk.Treeview.xview)
        vsb = ttk.Scrollbar(self.Frame2, orient="horizontal", command=listBox1.xview)
        vsb.place(relx=0.03, rely=0.96, relheight=0.025, relwidth=0.935)
        listBox1.configure(xscrollcommand=vsb.set)

        entries1()

        self.Frame3 = tk.Frame(self.Frame1)
        self.Frame3.place(relx=0.514, rely=0.118, relheight=0.833, relwidth=0.453)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#acffff")

        self.Label8 = tk.Label(self.Frame3)
        self.Label8.place(relx=0.411, rely=0.014, height=36, width=202)
        self.Label8.configure(background="#acffff")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font=font10)
        self.Label8.configure(foreground="#0000a0")
        self.Label8.configure(text='''Find Record''')

        self.Label9 = tk.Label(self.Frame3)
        self.Label9.place(relx=0.085, rely=0.085, height=36, width=113)
        self.Label9.configure(background="#acffff")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(font=font10)
        self.Label9.configure(foreground="#8080ff")
        self.Label9.configure(text='''Field''')


        self.TCombobox1 = ttk.Combobox(self.Frame3, textvariable=option, state='readonly')
        value_list = ['All Record', 'Id', 'Name', 'Branch', 'Designation', 'Email']
        self.TCombobox1.place(relx=0.34, rely=0.085, relheight=0.065
                              , relwidth=0.607)
        self.TCombobox1.configure(values=value_list)
        self.TCombobox1.configure(font="-family {Palatino Linotype} -size 14")
        option.set("Choose Category to Search")

        self.Label10 = tk.Label(self.Frame3)
        self.Label10.place(relx=0.057, rely=0.17, height=45, width=152)
        self.Label10.configure(background="#acffff")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(font=font10)
        self.Label10.configure(foreground="#8080ff")
        self.Label10.configure(text='''Value''')

        self.Entry6 = tk.Entry(self.Frame3, textvariable=value)
        self.Entry6.place(relx=0.34, rely=0.17,height=54, relwidth=0.601)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font=font13)
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(insertbackground="black")

        self.Button4 = tk.Button(self.Frame3, command=clear_frame2)
        self.Button4.place(relx=0.028, rely=0.298, height=53, width=196)
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(font=font10)
        self.Button4.configure(foreground="#0000a0")
        self.Button4.configure(text='''Clear''')

        self.Button4_3 = tk.Button(self.Frame3, command=search_btn)
        self.Button4_3.place(relx=0.355, rely=0.298, height=53, width=196)
        self.Button4_3.configure(background="#d9d9d9")
        self.Button4_3.configure(font="-family {Segoe UI} -size 18 -weight bold")
        self.Button4_3.configure(foreground="#0000a0")
        self.Button4_3.configure(text='''Find''')

        self.Button4_4 = tk.Button(self.Frame3, command=sam)
        self.Button4_4.place(relx=0.681, rely=0.298, height=53, width=196)
        self.Button4_4.configure(background="#d9d9d9")
        self.Button4_4.configure(font="-family {Segoe UI} -size 18 -weight bold")
        self.Button4_4.configure(foreground="#0000a0")
        self.Button4_4.configure(text='''Exit''')

        self.Text2 = tk.Text(self.Frame3)
        self.Text2.place(relx=0.028, rely=0.412, relheight=0.56, relwidth=0.942)
        self.Text2.configure(background="white")
        self.Text2.configure(font="TkTextFont")
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="#c4c4c4")
        self.Text2.configure(selectforeground="black")
        self.Text2.configure(wrap="word")

        global listBox2
        cols = ('Id', 'Name', 'Branch', 'Designation', 'Email')
        listBox2 = ttk.Treeview(self.Frame3, columns=cols, show='headings', selectmode='browse')
        for col in cols:
            listBox2.heading(col, text=col)
        listBox2.place(relx=0.028, rely=0.412, relheight=0.56, relwidth=0.942)
        # scrollbar = ttk.Scrollbar(orient=tk.HORIZONTAL, command=ttk.Treeview.xview)
        vsb = ttk.Scrollbar(self.Frame3, orient="horizontal", command=listBox2.xview)
        vsb.place(relx=0.03, rely=0.96, relheight=0.025, relwidth=0.935)
        listBox2.configure(xscrollcommand=vsb.set)

def sam():
    root.destroy()

def clear_frame1():
    id.set("")
    name.set("")
    branch.set("")
    designation.set("")
    email.set("")

def clear_frame2():
    option.set("Choose Category to Search")
    value.set("")

def save_record():
    id1 = id.get()
    name1 = name.get()
    branch1 = branch.get()
    designation1 = designation.get()
    email1 = email.get()
    query = 'insert into record values("{0}","{1}","{2}","{3}","{4}")'.format(id1, name1, branch1, designation1, email1)
    mycursor.execute(query)
    conn.commit()
    clear_frame1()
    entries1()

def delete_record():
    if (1):
        try:
            item_text = listBox1.focus()
            print(item_text)
            item_text = listBox1.item(item_text)['values'][0]
            print(item_text)
            # print(item_text)
        except:
            pass
    try:
        mycursor.execute("delete from record where rec_id='{0}'".format(item_text))
        conn.commit()
    except:
        pass
    entries1()

def search_btn():
    _entry = value.get()
    _option = option.get()

    if (_option == "Name"):
        listBox2.delete(*listBox2.get_children())
        mycursor.execute('select * from record where name like "%{0}%"'.format(_entry))
        for i in mycursor:
            listBox2.insert("", "end", values=i)
    elif (_option == "Id"):
        listBox2.delete(*listBox2.get_children())
        mycursor.execute('select * from record where rec_id="{0}"'.format(_entry))
        for i in mycursor:
            listBox2.insert("", "end", values=i)
    elif (_option == "Branch"):
        listBox2.delete(*listBox2.get_children())
        mycursor.execute('select * from record where branch like "%{0}%"'.format(_entry))
        for i in mycursor:
            listBox2.insert("", "end", values=i)
    elif (_option == "Designation"):
        listBox2.delete(*listBox2.get_children())
        mycursor.execute('select * from record where profession like "%{0}%"'.format(_entry))
        for i in mycursor:
            listBox2.insert("", "end", values=i)
    elif (_option == "Email"):
        listBox2.delete(*listBox2.get_children())
        mycursor.execute('select * from record where email like "%{0}%"'.format(_entry))
        for i in mycursor:
            listBox2.insert("", "end", values=i)
    elif (_option == "All Record"):
        listBox2.delete(*listBox2.get_children())
        mycursor.execute("select * from record")
        for i in mycursor:
            listBox2.insert("", "end", values=i)
    else:
        option.set("Choose Category Correctly")




def entries1():
    global listBox1
    listBox1.delete(*listBox1.get_children())
    mycursor.execute('select * from record')
    for i in mycursor:
        listBox1.insert("", "end", values=i)



if __name__ == '__main__':
    listBox1 = None
    root = tk.Tk()
    top = Toplevel1(root)
    root.mainloop()





