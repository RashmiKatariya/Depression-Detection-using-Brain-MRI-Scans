from tkinter import *
import sqlite3
import os
import sys
#import cv2
from PIL import ImageTk, Image
root = Tk()
root.geometry('500x500')
root.title("DEPRESSION DETECTION")
root.configure(background="#AC3B61")

uname=StringVar()
pwd=StringVar()

label_0 = Label(root, text="Depression Detection",bg="#AC3B61",fg="#FFFFFF", width=30,font=("Algerian", 20))
label_0.place(x=15,y=15)

label_1 = Label(root, text="Login Page",bg="#AC3B61",fg="#FFFFFF",width=30,font=("bold", 20))
label_1.place(x=8,y=50)



def database():
   name1=uname.get()
   name2=pwd.get()
   name3="x"
   name4="y"
   check=0
   conn = sqlite3.connect('depression_detect.db')
   with conn:
      cursor = conn.cursor()
   cursor.execute('SELECT * FROM user WHERE username=?  AND password=?',(name1,name2))
   result_set = cursor.fetchall()
   conn.commit()
   for row in result_set:
      name3=row[1]
      name4=row[4]
      check=check+1
   
   new='python detect.py --user1 '+name1+' --user2 '+name3+' --user3 '+name4
   print(new,"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
   if(check==0):
      print("............Login Not successfull")
   if(check==1):
      print("****************Login  successfull")
      os.system(new)
      #os.system('detect.py')
  
   
   
             
label_0 = Label(root, text="Login Form",bg="#AC3B61",fg="#FFFFFF", width=20,font=("bold", 12))
label_0.place(x=130,y=381)


label_1 = Label(root, text="UserName",bg="#AC3B61",fg="#FFFFFF",width=20,font=("bold", 10))
label_1.place(x=100,y=410)

entry_1 = Entry(root,textvar=uname)
entry_1.place(x=240,y=410)


label_2 = Label(root, text="Password",bg="#AC3B61",fg="#FFFFFF",width=20,font=("bold", 10))
label_2.place(x=100,y=440)

entry_2 = Entry(root,textvar=pwd)
entry_2.place(x=240,y=440)

#label_4 = Label(root, text="Programming",width=20,font=("bold", 10))
#label_4.place(x=85,y=330)
#var2= IntVar()
#Checkbutton(root, text="java", variable=var1).place(x=235,y=330)
#Checkbutton(root, text="python", variable=var2).place(x=290,y=330)
Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=470)

path = "d1.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(root, image = img,bg="#AC3B61")
panel.config( width=500 )
panel.config( height=250 )
panel.config( anchor="center" )
panel.place(x=8,y=10)
#panel.place(x=150,y=160)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "left",anchor="center")#side = "up", fill = "both", expand = "yes")

root.mainloop()























