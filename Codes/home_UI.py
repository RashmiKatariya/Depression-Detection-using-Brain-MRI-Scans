from tkinter import *
import sqlite3
import sys
import os
from PIL import ImageTk, Image
import cv2

root = Tk()
root.geometry('500x500')
root.title("DEPRESSION DETECTION USING MACHINE LEARNING")
root.configure(background="#AC3B61")

uname=StringVar()
pwd=StringVar()


def run1():
    os.system('depress_f.py')

def run2():
   os.system('depress_s.py')
   
   
             
label_0 = Label(root, text="Depression Detection",width=30,font=("Algerian", 20),fg="#FFFFFF",bg="#AC3B61")
label_0.place(x=15,y=15)

label_1 = Label(root, text="Home Page",fg="#FFFFFF",bg="#AC3B61",width=30,font=("bold", 20))
label_1.place(x=8,y=50)

#label_1 = Label(root, text="UserName",width=20,font=("bold", 10))
#label_1.place(x=80,y=130)

#entry_1 = Entry(root,textvar=uname)
#entry_1.place(x=240,y=130)




#label_4 = Label(root, text="Programming",width=20,font=("bold", 10))
#label_4.place(x=85,y=330)
#var2= IntVar()
#Checkbutton(root, text="java", variable=var1).place(x=235,y=330)
#Checkbutton(root, text="python", variable=var2).place(x=290,y=330)
Button(root, text='Login',width=20,bg='brown',fg='white',command=run1).place(x=120,y=400)

Button(root, text='Signup',width=20,bg='brown',fg='white',command=run2).place(x=240,y=400)


path = "d1.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(root, image = img,bg="#AC3B61")
panel.config( width=500 )
panel.config( height=300 )
panel.config( anchor="center" )
#panel.place(x=150,y=160)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "left",anchor="center")#side = "up", fill = "both", expand = "yes")


root.mainloop()























