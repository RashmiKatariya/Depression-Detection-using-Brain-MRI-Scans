from tkinter import *
import sqlite3
import os
import sys

root = Tk()
root.geometry('500x500')
root.title("DEPRESSION DETECTION")
root.configure(background="#AC3B61")


fname=StringVar()
lname=StringVar()
Email=StringVar()
var = IntVar()
c=StringVar()
uname=StringVar()
pwd=StringVar()



def database():
   name1=fname.get()
   name2=lname.get()
   email=Email.get()
   gender=var.get()
   country=c.get()
   uname1=uname.get()
   pwd1=pwd.get()
   conn = sqlite3.connect('depression_detect.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS user (fname TEXT,lname TEXT,email TEXT,gender TEXT,country TEXT,username TEXT,password TEXT)')
   cursor.execute('INSERT INTO user (fname,lname,email,gender,country,username,password) VALUES(?,?,?,?,?,?,?)',(name1,name2,email,gender,country,uname1,pwd1))
   conn.commit()
   os.system('depress_f.py')
   
   
   
label_0 = Label(root, text="Depression Detection",bg="#AC3B61",width=30,font=("Algerian", 20),fg="#FFFFFF")
label_0.place(x=15,y=15)

label_0 = Label(root, text="User Registration Form",bg="#AC3B61",fg="#FFFFFF",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="First Name",bg="#AC3B61",fg="#FFFFFF",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=fname,bg="#AC3B61")
entry_1.place(x=240,y=130)


label_1 = Label(root, text="Last Name",bg="#AC3B61",fg="#FFFFFF",width=20,font=("bold", 10))
label_1.place(x=80,y=160)

entry_1 = Entry(root,textvar=lname,bg="#AC3B61")
entry_1.place(x=240,y=160)



label_2 = Label(root, text="Email",bg="#AC3B61",fg="#FFFFFF",width=20,font=("bold", 10))
label_2.place(x=68,y=190)

entry_2 = Entry(root,textvar=Email,bg="#AC3B61")
entry_2.place(x=240,y=190)

label_3 = Label(root, text="Gender",width=20,bg="#AC3B61",fg="#FFFFFF",font=("bold", 10))
label_3.place(x=70,y=220)

Radiobutton(root, text="Male",padx = 5, variable=var, value=1,bg="#AC3B61").place(x=235,y=220)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2,bg="#AC3B61").place(x=290,y=220)

label_4 = Label(root, text="country",bg="#AC3B61",fg="#FFFFFF",width=20,font=("bold", 10))
label_4.place(x=70,y=250)

list1 = ['America','India','UK','Nepal','China','South Africa'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your country') 
droplist.place(x=240,y=250)

label_22 = Label(root, text="Username",bg="#AC3B61",fg="#FFFFFF",width=20,font=("bold", 10))
label_22.place(x=80,y=300)

entry_22 = Entry(root,textvar=uname,bg="#AC3B61")
entry_22.place(x=240,y=300)


label_33 = Label(root, text="Password",bg="#AC3B61",fg="#FFFFFF",width=20,font=("bold", 10))
label_33.place(x=80,y=330)

entry_33 = Entry(root,textvar=pwd,bg="#AC3B61")
entry_33.place(x=240,y=330)

#label_4 = Label(root, text="Programming",width=20,font=("bold", 10))
#label_4.place(x=85,y=330)
#var2= IntVar()
#Checkbutton(root, text="java", variable=var1).place(x=235,y=330)
#Checkbutton(root, text="python", variable=var2).place(x=290,y=330)
Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=360)

root.mainloop()























