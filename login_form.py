#Registration form with database using place
#user interface
from tkinter import *
import sqlite3
root=Tk()
root.geometry("500x500")
root.resizable(0,0)
root.title("Registration Form")
FullName=StringVar()
Email=StringVar()
var=IntVar()
c=StringVar()
var1=IntVar()
from tkinter import messagebox
def not_allowed():
    messagebox.showinfo("Gui","All fields are manadatory")
    
def check():
    messagebox.showinfo("Gui","Data saved successfully")
    
def Database():
    name1=FullName.get()
    email=Email.get()
    gender=var.get()
    if gender==1:
        gender="Male"
    else:
        gender="Female"
    country=c.get()
    prog=var1.get()
    if prog==1:
        prog="Java"
    else:
        prog="Python"
    if name1=="" and email=="" and gender=="Male" or gender=="Female" and country=="select your country" and prog=="Python" or prog=="Java":
        not_allowed()
    else:
        conn=sqlite3.connect('form.db')
        with conn:
            cursor=conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS student (Fullname Text)')
            cursor.execute('INSERT INTO student(Fullname,Email,Gender,Country,Programming)VALUES(?,?,?,?,?)',(name1,email,gender,country,prog))
            conn.commit()
            check()
                           
label_0=Label(root,text="Registration form",width=20,font=("bold",20))
label_0.place(x=90,y=53)
label_1=Label(root,text="FullName",width=20,font=("bold",10))
label_1.place(x=80,y=130)
entry_1=Entry(root,textvar=FullName)
entry_1.place(x=240,y=130)
label_2=Label(root,text="Email",width=20,font=("bold",10))
label_2.place(x=68,y=180)
entry_2=Entry(root,textvar=Email)
entry_2.place(x=240,y=180)
label_3=Label(root,text="Gender",width=20,font=("bold",10))
label_3.place(x=70,y=230)
Radiobutton(root,text="Male",variable=var,value=1).place(x=235,y=230)
Radiobutton(root,text="Female",variable=var,value=2).place(x=290,y=230)
label_4=Label(root,text="city",width=20,font=("bold",10))
label_4.place(x=70,y=280)
list1=["Roorkee","UP","Meerut","Rudrapur","Haldwani","None"]
droplist=OptionMenu(root,c,*list1)#lagana jruri h
droplist.config(width=15)
c.set("select your city")
droplist.place(x=240,y=280)
label_5=Label(root,text="programming",width=20,font=("bold",10))
label_5.place(x=85,y=330)
var2=IntVar()
Checkbutton(root,text="java",variable=var1).place(x=235,y=330)
Checkbutton(root,text="python",variable=var2).place(x=290,y=330)
Button(root,text="submit",width=20,bg="brown",fg="white",command=Database).place(x=180,y=380)
root.mainloop()

    